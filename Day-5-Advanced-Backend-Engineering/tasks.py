
import time

from celery_config import celery_app


@celery_app.task(
    bind=True,
    max_retries=3
)
def generate_note_summary(self, note_id: int):
    try:
        # Simulate a time-consuming task
        print(f"Generating summary for note ID: {note_id}")

        time.sleep(5)

        summary = f"Summary generated for note {note_id}"

        print(summary)

        return {
            "note_id": note_id,
            "summary": summary,
            "status": "completed"
        }

    except Exception as error:
        # Retry the task if an error occurs
        raise self.retry(
            exc=error,
            countdown=5
        )
