import asyncio
import json
from asyncio import StreamReader, StreamWriter
from enum import Enum
from typing import Union

from aiortc import RTCIceCandidate, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp, candidate_to_sdp

from rtc.model.signaling import MessageType

BYE = object()



def object_from_string(message_str:str):
    message = json.loads(message_str)
    if message["type"] in [MessageType.answer.value, MessageType.offer.value]:
        return RTCSessionDescription(**message)
    elif message["type"] == "bye":
        return BYE


def object_to_string(obj: Union[BYE,RTCSessionDescription]):
    if isinstance(obj, RTCSessionDescription):
        message = {"sdp": obj.sdp, "type": obj.type}
    else:
        assert obj is BYE
        message = {"type": "bye"}
    return json.dumps(message, sort_keys=True)


class TcpSocketSignaling:
    def __init__(self, host: str, port:str):
        self._host = host
        self._port = port

    async def recieve(self):
        def client_connected(reader: StreamReader, writer: StreamWriter):
            try:
                data = reader.readuntil()
            except asyncio.IncompleteReadError:
                return object_from_string(data.decode("utf8"))
        async with asyncio.start_server(
            client_connected, host=self._host, port=self._port
        ) as server:
            await server.serve_forever()


    async def send(self, descr):
        writer = await asyncio.open_connection(
            host=self._host, port=self._port
        )
        data = object_to_string(descr).encode("utf8")
        self._writer.write(data + b"\n")
