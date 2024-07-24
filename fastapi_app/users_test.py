from fastapi.testclient import TestClient
from unittest.mock import patch

from .main import app
from fastapi_app import crud

client = TestClient(app)

test_users = [
    {
        "id": 1,
        "username": "user",
        "email": "user@mail.com",
        "created_at": "2024-07-23T12:39:21.279334Z",
        "updated_at": None,
        "team_id": None
    },
    {
        "id":2,
        "username": "admin",
        "email": "admin@mail.com",
        "created_at": "2024-07-23T12:39:21.279334Z",
        "updated_at": None,
        "team_id": None
    }
]

def test_get_users():
    with patch('fastapi_app.crud.get_users') as mock_get_users:
        mock_get_users.return_value = test_users
        response = client.get("/users")
        assert response.status_code == 200
        assert response.json() == test_users

def test_get_users_empty():
    with patch('fastapi_app.crud.get_users') as mock_get_users:
        mock_get_users.return_value = []
        response = client.get("/users")
        assert response.status_code == 200
        assert response.json() == []

def test_get_user_by_id():
    with patch('fastapi_app.crud.get_user') as mock_get_user_by_id:
        mock_get_user_by_id.return_value = test_users[0]
        response = client.get("/users/1")
        assert response.status_code == 200
        assert response.json() == test_users[0]

def test_get_non_existent_user():
    with patch('fastapi_app.crud.get_user') as mock_get_user_by_id:
        mock_get_user_by_id.return_value = None  # Предполагаем, что несуществующий пользователь возвращает None
        response = client.get("/users/999")
        assert response.status_code == 404  # Предполагаем, что несуществующий пользователь возвращает 404