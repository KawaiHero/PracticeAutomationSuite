import pytest

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

def test_get_wrong_id(client):
    response = client.get(Endpoints.POSTS + "/9999")
    assert response.status_code == 404, 'Expected 404 for non-existent post'

@pytest.mark.parametrize('id', ['1','2','3'])
def test_get_post_by_id(client, id):
    response = client.get(Endpoints.POSTS + "/" + id)
    assert response.status_code == 200
    data = response.json()
    assert "id"  in data
    assert "title" in data
    assert "body" in data