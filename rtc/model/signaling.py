from enum import Enum

from pydantic import BaseModel


class MessageType(Enum):
    answer = "answer"
    offer = "offer"
    bye = "bye"


class Offer(BaseModel):
    type: MessageType
    sdp: str
