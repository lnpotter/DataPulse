from fastapi import FastAPI, WebSocket
from .routes import router
from .websocket import websocket_endpoint

app = FastAPI()

app.include_router(router)

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)
