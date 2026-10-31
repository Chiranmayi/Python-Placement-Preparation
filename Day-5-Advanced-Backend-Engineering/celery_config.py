
from celery import Celery

# Create Celery application
celery_app = Celery(
    "notes_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)
# Broker (/0): Sends tasks to workers.
# Backend (/1): Stores task results and status.

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
    task_track_started=True
)
