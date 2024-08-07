import fastapi
from rtc.routers.static import HTMLRouterFactory

def create_app():
    app = fastapi.FastAPI()
    
    app.add_api_route(
        HTMLRouterFactory().create_router()
    )
    
    return app
