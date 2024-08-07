from aiortc import RTCPeerConnection,RTCSessionDescription
from aiortc.contrib.media import MediaRecorder
import logging

logger = logging.getLogger(__name__)


class RTCMedia:
    def __init__(self):
        self.recorder = MediaRecorder()
        self.pc = RTCPeerConnection()

    async def handle_offer(self, offer: RTCSessionDescription):
        await self.pc.setRemoteDescription(offer)

    async def answer(self):
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)
        return answer
    

    def register_events():
        pc.
        @self.pc.on("track")
        def on_track(track):
            logger.info("Track %s received", track.kind)

            if track.kind == "audio":
                pc.addTrack(player.audio)
                recorder.addTrack(track)
            elif track.kind == "video":
                pc.addTrack(
                    VideoTransformTrack(
                        relay.subscribe(track), transform=params["video_transform"]
                    )
                )
                if args.record_to:
                    recorder.addTrack(relay.subscribe(track))

            @track.on("ended")
            async def on_ended():
                log_info("Track %s ended", track.kind)
                await recorder.stop()