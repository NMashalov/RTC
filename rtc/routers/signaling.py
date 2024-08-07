from fastapi import APIRouter
from rtc.handlers.signaling import SignalingHandler


class HTMLRouterFactory:
    SIGNALING_PATH: str = "signaling"
    STATIC_PREFIX: str = "/signaling"
    TAGS = ["signaling"]

    def __init__(self, handler: SignalingHandler):
        self._handler = handler

    def create_router(self):
        router = APIRouter(prefix=self.STATIC_PREFIX, tags=self.TAGS)
        router.add_api_route(
            path=self.SIGNALING_PATH, endpoint=self._handler.start, methods=["POST"]
        )
        return router
