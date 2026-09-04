# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : API Testing
#  Author       : Team Tinitiate
# ==============================================================================



import requests

base_url = "https://jsonplaceholder.typicode.com"

# Test GET request
def test_get_posts():
    response = requests.get(base_url + "/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test POST request (Successful)
def test_create_post_success():
    payload = {
        "userId": 1,
        "id": 101,
        "title": "test title",
        "body": "test body"
    }
    response = requests.post(base_url + "/posts", json=payload)
    assert response.status_code == 201

# Test POST request (Failure)
def test_create_post_failure():
    payload = {
        "userId": 1,
        "id": 101,  # This ID already exists, causing failure
        "title": "test title",
        "body": "test body"
    }
    response = requests.post(base_url + "/posts", json=payload)
    assert response.status_code == 500  # Assuming the API returns a 500 error

# Test GET request (Failure)
def test_get_post_failure():
    non_existent_post_id = 9999
    response = requests.get(base_url + f"/posts/{non_existent_post_id}")
    assert response.status_code == 404

# Test PUT request
def test_update_post():
    post_id = 1
    updated_payload = {
        "title": "updated title",
        "body": "updated body"
    }
    response = requests.put(base_url + f"/posts/{post_id}", json=updated_payload)
    assert response.status_code == 200
    assert response.json()["title"] == updated_payload["title"]

# Test DELETE request
def test_delete_post():
    post_id = 1
    response = requests.delete(base_url + f"/posts/{post_id}")
    assert response.status_code == 200

# Test request with query parameters
def test_get_posts_with_query_params():
    query_params = {"userId": 1}
    response = requests.get(base_url + "/posts", params=query_params)
    assert response.status_code == 200
    for post in response.json():
        assert post["userId"] == query_params["userId"]
