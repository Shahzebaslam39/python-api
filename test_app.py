import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test if the home page says Hello Shahzeb"""
    response = client.get("/")
    assert response.data == b"Hello Shahzeb"

def test_health(client):
    """Test if the /health page says OK"""
    response = client.get("/health")
    assert response.data == b"OK"