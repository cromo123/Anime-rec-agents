from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_recommend_returns_structured_response() -> None:
    response = client.post(
        "/recommend",
        json={
            "user_id": "beginner-user",
            "message": "I want something thoughtful",
            "mood": "curious",
            "available_time": "a few weeks",
            "disliked_genres": [],
            "preferred_genres": [],
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert "recommended_anime" in body
    assert "confidence" in body
    assert "reason" in body
    assert "watch_plan" in body
    assert "agents_used" in body


def test_psychological_request_returns_psycho_pass() -> None:
    response = client.post(
        "/recommend",
        json={
            "user_id": "beginner-user",
            "message": "I want a psychological thriller",
        },
    )

    assert response.status_code == 200
    assert response.json()["recommended_anime"] == "Psycho-Pass"
