
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from database import engine, Base
from routers.notes import router as notes_router
from websocket_manager import manager
from rate_limiter import rate_limit
from tasks import generate_note_summary
from celery.result import AsyncResult
from celery_config import celery_app


# Create database tables
Base.metadata.create_all(bind=engine)


# Application lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Notes API starting...")

    yield

    print("Notes API shutting down...")


# Create FastAPI application
app = FastAPI(
    title="Day 5 - Advanced Backend Engineering",
    description="Notes API with CRUD, security, WebSockets and background tasks",
    version="1.0.0",
    lifespan=lifespan
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Register notes router
app.include_router(
    notes_router,
    prefix="/v1"
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Day 5 Advanced Backend Engineering API"
    }


# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Rate-limited endpoint for demonstration
@app.get("/rate-limit-demo")
async def rate_limit_demo(
    _: None = Depends(rate_limit)
):
    return {
        "message": "Request successful"
    }


# WebSocket endpoint
@app.websocket("/ws/notes/{room}")
async def notes_websocket(
    websocket: WebSocket,
    room: str
):
    await manager.connect(websocket, room)

    try:
        while True:
            message = await websocket.receive_text()

            await manager.broadcast(
                message=message,
                room=room
            )

    except WebSocketDisconnect:
        manager.disconnect(websocket, room)


# Create background summary task
@app.post("/v1/notes/{note_id}/summary", status_code=202)
def request_summary(note_id: int):
    task = generate_note_summary.delay(note_id)

    return {
        "task_id": task.id,
        "status": "queued"
    }


# Check background task status
@app.get("/v1/tasks/{task_id}")
def check_task_status(task_id: str):
    result = AsyncResult(
        task_id,
        app=celery_app
    )

    return {
        "task_id": task_id,
        "state": result.state,
        "ready": result.ready()
    }
