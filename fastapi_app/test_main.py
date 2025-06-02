from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

name = str(uuid.uuid4())
email = f"user_{str(uuid.uuid4())}@example.com"

def test_post_users():
    
    response = client.post(
        "/users/",
        json={"name": name, "email": email},
    )
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["email"] == email


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    assert data[-1]["name"] == name
    assert data[-1]["email"] == email