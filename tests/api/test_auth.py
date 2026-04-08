def test_register(client):
    response = client.post("/v1/auth/register", json={"email": "a@b.com", "password": "secret123"})
    assert response.status_code == 200


def test_login(client):
    response = client.post("/v1/auth/login", json={"email": "a@b.com", "password": "secret123"})
    assert response.status_code == 200
