
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


DAY4_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DAY4_FOLDER))

from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_async_status(client):
    response = client.get("/async-status")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_get_products(client):
    response = client.get("/api/v1/products/")

    assert response.status_code == 200
    assert len(response.json()["products"]) == 3


def test_get_product(client):
    response = client.get("/api/v1/products/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_user_profile(client):
    response = client.get("/api/v1/users/profile")

    assert response.status_code == 200
    assert response.json()["user"]["username"] == "Chiranmayi"


def test_admin_dashboard(client):
    response = client.get("/api/v1/users/admin")

    assert response.status_code == 200
    assert response.json()["role"] == "admin"


def test_timing_middleware(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "X-Process-Time" in response.headers


def test_lifecycle(client):
    response = client.get("/lifecycle")

    assert response.status_code == 200
    assert response.json()["application_ready"] is True
