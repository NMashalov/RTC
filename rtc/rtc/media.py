from aiortc import RTCPeerConnection, RTCSessionDescription, RTCDataChannel
from aiortc.contrib.media import MediaRecorder, MediaRelay
from aiortc.mediastreams import MediaStreamTrack
import logging

logger = logging.getLogger(__name__)


class PingPong:
    def on_datachannel(channel: RTCDataChannel):
        @channel.on("message")
        def on_message(message: str):
            if message.startswith("ping"):
                channel.send("pong" + message[4:])


class RTCMedia:
    def __init__(self):
        self.recorder = MediaRecorder()
        self.relay = MediaRelay()
        self.pc = RTCPeerConnection()
        self.player = None
        self.pc.createDataChannel()

    def on_track(self, track: MediaStreamTrack):
        logger.info("Track %s received", track.kind)
        if track.kind == "audio":
            self.pc.addTrack(self.player.audio)
        elif track.kind == "video":
            self.pc.addTrack(self.relay.subscribe(track))
            self.recorder.addTrack(self.relay.subscribe(track))

            @track.on("ended")
            async def on_ended():
                logger.info("Track %s ended", track.kind)
                await self.recorder.stop()


class Connection:
    def __init__(self):
        self.pc = RTCPeerConnection()

    async def handle_offer(self, offer: RTCSessionDescription):
        await self.pc.setRemoteDescription(offer)

    async def answer(self):
        answer = await self.pc.createAnswer()
        await self.pc.setLocalDescription(answer)
        return answer

    def register_media_events(self):
        self.pc.add_listener(event="track", f=RTCMedia().on_track)

    def register_datachannel_events(self):
        self.pc.add_listener(event="datacahnnel", f=PingPong().on_datachannel)
