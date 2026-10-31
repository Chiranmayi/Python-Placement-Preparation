
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


DAY5_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DAY5_FOLDER))

from main import app
from database import Base, engine
from rate_limiter import rate_limit


# Test setup
@pytest.fixture
def client():
    # Create a clean database for each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Disable rate limiting during tests
    app.dependency_overrides[rate_limit] = lambda: None

    with TestClient(app) as test_client:
        yield test_client

    # Clean up dependency overrides
    app.dependency_overrides.clear()


API_KEY = {
    "X-API-Key": "day5-secret-key"
}


# Test home endpoint
def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


# Test health endpoint
def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# Test creating a note
def test_create_note(client):
    response = client.post(
        "/v1/notes/",
        headers=API_KEY,
        json={
            "title": "Learn FastAPI",
            "body": "Practice backend development",
            "status": "draft"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn FastAPI"


# Test getting all notes
def test_get_notes(client):
    client.post(
        "/v1/notes/",
        headers=API_KEY,
        json={"title": "Python", "body": "Learn Python"}
    )

    response = client.get(
        "/v1/notes/",
        headers=API_KEY
    )

    assert response.status_code == 200
    assert response.json()["total"] == 1


# Test getting one note
def test_get_single_note(client):
    create_response = client.post(
        "/v1/notes/",
        headers=API_KEY,
        json={"title": "SQL", "body": "Learn SQL"}
    )

    note_id = create_response.json()["id"]

    response = client.get(
        f"/v1/notes/{note_id}",
        headers=API_KEY
    )

    assert response.status_code == 200
    assert response.json()["title"] == "SQL"


# Test updating a note
def test_update_note(client):
    create_response = client.post(
        "/v1/notes/",
        headers=API_KEY,
        json={"title": "Python"}
    )

    note_id = create_response.json()["id"]

    response = client.patch(
        f"/v1/notes/{note_id}",
        headers=API_KEY,
        json={"title": "Advanced Python"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Advanced Python"


# Test deleting a note
def test_delete_note(client):
    create_response = client.post(
        "/v1/notes/",
        headers=API_KEY,
        json={"title": "Delete me"}
    )

    note_id = create_response.json()["id"]

    response = client.delete(
        f"/v1/notes/{note_id}",
        headers=API_KEY
    )

    assert response.status_code == 204


# Test note not found
def test_note_not_found(client):
    response = client.get(
        "/v1/notes/999",
        headers=API_KEY
    )

    assert response.status_code == 404


# Test missing API key
def test_missing_api_key(client):
    response = client.get("/v1/notes/")

    assert response.status_code == 401


# Test invalid API key
def test_invalid_api_key(client):
    response = client.get(
        "/v1/notes/",
        headers={"X-API-Key": "wrong-key"}
    )

    assert response.status_code == 401


# Test invalid pagination
def test_invalid_limit(client):
    response = client.get(
        "/v1/notes/?limit=200",
        headers=API_KEY
    )

    assert response.status_code == 422
