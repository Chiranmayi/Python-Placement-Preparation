# Day 5 – Advanced Backend Engineering

## Project: Notes API using FastAPI

### 1. Project Overview

This project implements a Notes API using FastAPI and SQLAlchemy. It demonstrates advanced backend engineering concepts, including CRUD operations, API-key authentication, rate limiting, pagination, searching, sorting, WebSockets, background task processing, and automated testing.

### 2. Technologies Used


- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- HTTPX
- WebSockets
- Celery
- Redis

### 3. Project Structure


Day-5-Advanced-Backend-Engineering/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── dependencies.py
├── security.py
├── rate_limiter.py
├── websocket_manager.py
├── celery_config.py
├── tasks.py
├── requirements.txt
├── README.md
│
├── routers/
│   ├── __init__.py
│   └── notes.py
│
└── tests/
    ├── __init__.py
    └── test_notes.py


### 4. Features Implemented

CRUD Operations
- Create a note.
- Retrieve all notes.
- Retrieve a note by ID.
- Update an existing note.
- Delete a note.

Search, Pagination and Sorting
- Search notes by title.
- Filter notes by status.
- Limit the number of returned records.
- Skip records using offset.
- Sort using approved fields.

API Security
- API-key authentication using request headers.
- Missing and invalid API-key validation.
- Secure comparison of API keys.

Rate Limiting
- Limits requests to 5 per 60-second window per client IP.
- Returns HTTP 429 when the limit is exceeded.
- Includes a Retry-After response header.

WebSockets
- Persistent two-way communication.
- Room-based connection management.
- Broadcasting messages to room members.
- Disconnect cleanup.

Background Tasks
- Celery task for generating note summaries.
- Redis as the message broker and result backend.
- Task ID and task status endpoint.
- Retry configuration for failed tasks.

Automated Testing
- Pytest and FastAPI TestClient.
- CRUD endpoint testing.
- Authentication testing.
- Missing-resource testing.
- Pagination validation testing.

### 5. Installation and Setup

Clone the repository:

bash
git clone https://github.com/Chiranmayi/Python-Placement-Preparation.git


Navigate to the Day 5 folder:

bash
cd Python-Placement-Preparation/Day-5-Advanced-Backend-Engineering


Install dependencies:

bash
python -m pip install -r requirements.txt


### 6. Run the Application

Start the FastAPI server:

bash
uvicorn main:app --reload


Open Swagger UI:

text
http://127.0.0.1:8000/docs


### 7. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/v1/notes/` | Create a note |
| GET | `/v1/notes/` | Retrieve notes |
| GET | `/v1/notes/{note_id}` | Retrieve one note |
| PATCH | `/v1/notes/{note_id}` | Update a note |
| DELETE | `/v1/notes/{note_id}` | Delete a note |
| GET | `/rate-limit-demo` | Test rate limiting |
| WS | `/ws/notes/{room}` | WebSocket communication |
| POST | `/v1/notes/{note_id}/summary` | Queue summary task |
| GET | `/v1/tasks/{task_id}` | Check task status |

### 8. API Authentication

Protected Notes endpoints require an API key in the request header.

text
X-API-Key: day5-secret-key


The default key is for local learning and testing only. Production applications should use securely managed secrets.

### 9. Sample Request

Create a note:

json
{
    "title": "Learn FastAPI",
    "body": "Practice advanced backend engineering",
    "status": "draft"
}


Example response:

json
{
    "id": 1,
    "title": "Learn FastAPI",
    "body": "Practice advanced backend engineering",
    "status": "draft"
}


### 10. Running Tests

Run the automated tests:

bash
pytest -q

Latest test result:

text
11 passed, 1 warning


The remaining warning concerns the deprecated HTTPX integration used by the installed Starlette TestClient.

### 11. Background Worker Setup

Redis must be installed and running before using Celery background tasks.

Start the Celery worker from the Day 5 project directory:

bash
celery -A celery_config.celery_app worker --loglevel=info --pool=solo


The `--pool=solo` option is useful for local development on Windows.

### 12. HTTP Status Codes Used

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 202 | Background task accepted |
| 204 | Successful deletion |
| 400 | Invalid request |
| 401 | Unauthorized |
| 404 | Resource not found |
| 422 | Validation error |
| 429 | Too many requests |
| 500 | Internal server error |

### 13. Known Limitations

- SQLite is used for local development.
- The rate limiter uses in-memory storage and is not shared across multiple workers.
- The WebSocket manager uses in-memory connections and supports a single-process demonstration.
- Redis and Celery require separate setup and have not been covered by the 11 automated tests.
- The summary task currently simulates processing rather than generating an actual AI summary.
- The default API key is intended only for local learning.

### 14. Learning Outcomes

Through this project, I practiced:

- Designing REST APIs using FastAPI.
- Implementing CRUD operations with SQLAlchemy.
- Validating data using Pydantic.
- Implementing API-key authentication.
- Applying rate limiting.
- Implementing pagination, filtering and sorting.
- Managing WebSocket connections and broadcasting.
- Understanding Celery and Redis background processing.
- Writing automated API tests using Pytest.
- Organizing backend applications into separate modules.

