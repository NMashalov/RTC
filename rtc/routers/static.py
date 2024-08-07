from fastapi import APIRouter

class HTMLRouterFactory:
    STATIC_PATH: str = "rtc/static/"
    STATIC_PREFIX: str = "/static"
    TAGS=['static']

    def create_router(self):
        router = APIRouter(prefix=self.STATIC_PREFIX,tags=self.TAGS)
        router.add_api_route(
            methods=['GET']
        )
        return router
