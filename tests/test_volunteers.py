def test_create_valid_volunteer(client):
    """Should create volunteer with valid data"""

    payload = {
        "name": "João Silva",
        "email": "joao@email.com",
        "phone": "21999999999",
        "desired_position": "backend",
        "availability": "weekend",
    }

    response = client.post("/volunteers", json=payload)

    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]


def test_do_not_allow_duplicate_email(client):
    """Should not allow registering with duplicate email"""

    payload = {
        "name": "João Silva",
        "email": "joao@email.com",
        "phone": "21999999999",
        "desired_position": "backend",
        "availability": "weekend",
    }

    response_first = client.post("/volunteers", json=payload)
    assert response_first.status_code == 200

    response_second = client.post("/volunteers", json=payload)
    assert response_second.status_code == 400
    assert response_second.json()["detail"] == "Email already registered."
