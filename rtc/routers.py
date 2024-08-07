from fastapi import APIRouter

class HTMLRouterFactory:
    STATIC_PATH: str = 'rtc/static/'
    STATIC_PREFIX: str = '/static'

    def create_router(self):
        router = APIRouter(prefix=self.STATIC_PREFIX)

        router.add_api_route(
        )

        return router
