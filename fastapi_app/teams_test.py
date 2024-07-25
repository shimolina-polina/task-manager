from fastapi.testclient import TestClient
from unittest.mock import patch

from .main import app
from fastapi_app import crud

client = TestClient(app)

test_teams = [
    {
        "name": "DreamTeam",
        "id": 1,
        "created_at": "2024-07-24T15:49:20.734248Z",
        "updated_at": None
    },
    {
        "name": "BadTeam",
        "id": 2,
        "created_at": "2024-07-24T15:49:20.734248Z",
        "updated_at": None
    }
]

def test_get_teams():
    with patch('fastapi_app.crud.get_teams') as mock_get_teams:
        mock_get_teams.return_value = test_teams
        response = client.get("/teams")
        assert response.status_code == 200
        assert response.json() == test_teams

def test_get_teams_empty():
    with patch('fastapi_app.crud.get_teams') as mock_get_teams:
        mock_get_teams.return_value = []
        response = client.get("/teams")
        assert response.status_code == 200
        assert response.json() == []

def test_get_team_by_id():
    with patch('fastapi_app.crud.get_team') as mock_get_team_by_id:
        mock_get_team_by_id.return_value = test_teams[0]
        response = client.get("/teams/1")
        assert response.status_code == 200
        assert response.json() == test_teams[0]

def test_get_non_existent_team():
    with patch('fastapi_app.crud.get_user') as mock_get_team_by_id:
        mock_get_team_by_id.return_value = None 
        response = client.get("/teams/999")
        assert response.status_code == 404