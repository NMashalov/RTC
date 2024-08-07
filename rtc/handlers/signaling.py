from aiortc import RTCSessionDescription

from rtc.model.signaling import Offer
from rtc.rtc.media import RTCMedia


class SignalingHandler:
    def __init__(self):
        self.rtc_media = RTCMedia()

    async def start(self, offer: Offer):
        offer = RTCSessionDescription(sdp=Offer.sdp, type=params["type"])

        await self.rtc_media
