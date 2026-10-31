import asyncio
from time import perf_counter
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from routers import products, users


# Task F: Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Application starting...")

    app.state.ready = True

    yield

    app.state.ready = False

    print("Application shutting down...")


app = FastAPI(
    title="Day 4 - Async and Middleware API",
    description="Python Placement Preparation Series",
    version="1.0.0",
    lifespan=lifespan
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)


# Task C: Timing Middleware
@app.middleware("http")
async def timing_middleware(request: Request, call_next):

    start_time = perf_counter()

    response = await call_next(request)

    process_time = perf_counter() - start_time

    response.headers["X-Process-Time"] = str(
        round(process_time, 6)
    )

    return response


# Register routers
app.include_router(products.router, prefix="/api/v1")

app.include_router(users.router, prefix="/api/v1")


# Task B: Async endpoint
@app.get("/async-status")
async def async_status():

    await asyncio.sleep(1)

    return {
        "message": "Async endpoint working successfully",
        "status": "ready"
    }


# Task F: Background task
def send_notification(username: str):

    print(f"Notification sent to {username}")


@app.post("/send-notification")
def create_notification(
    background_tasks: BackgroundTasks,
    username: str
):

    background_tasks.add_task(
        send_notification,
        username
    )

    return {
        "message": "Notification request accepted",
        "username": username
    }


# Health check
@app.get("/")
def home():

    return {
        "message": "Welcome to Day 4 FastAPI Assignment",
        "status": "running"
    }


# Lifespan status
@app.get("/lifecycle")
def lifecycle_status(request: Request):

    return {
        "application_ready": request.app.state.ready
    }