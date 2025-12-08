from api.endpoints import Endpoints

def test_get_posts_list(client):
    response = client.get(Endpoints.POSTS)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_post(client):
    response = client.get(Endpoints.POSTS + "/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_post(client):
    payload = {
        "title": "test title",
        "body": "content",
        "userId": 1
    }

    response = client.post(Endpoints.POSTS, json=payload)
    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_delete_post(client):
    response = client.delete(Endpoints.POSTS + "/1")
    assert response.status_code == 200 or response.status_code == 204