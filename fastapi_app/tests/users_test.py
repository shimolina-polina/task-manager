from fastapi.testclient import TestClient

from fastapi_app.main import app

from fastapi_app import crud

client = TestClient(app)

test_users = [
    {"id": 1, "username": "Alice", "email": "alice@example.com"},
    {"id": 2, "username": "Bob", "email": "bob@example.com"},
]

def override_get_users():
    return test_users

app.dependency_overrides[crud.get_users] = override_get_users

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == test_users

def test_get_users_empty():
    # Переопределим зависимость, чтобы вернуть пустой список пользователей
    app.dependency_overrides[crud.get_users] = lambda: []

    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []

    # Вернем зависимость обратно
    app.dependency_overrides = {}

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == test_users[0]

def test_get_non_existent_user():
    response = client.get("/users/999")
    assert response.status_code == 404  # Предполагаем, что несуществующий пользователь возвращает 404