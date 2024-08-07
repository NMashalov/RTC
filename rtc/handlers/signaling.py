from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription


class Signaling:
    def __init__(self):
        pass

    def start():

        offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

        pc = RTCPeerConnection()
        pc_id = "PeerConnection(%s)" % uuid.uuid4()
        pcs.add(pc)