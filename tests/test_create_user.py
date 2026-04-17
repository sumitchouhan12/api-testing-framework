from utils.api_client import create_user

def test_create_user():
    response = create_user("Sumit", "QA Engineer")

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Sumit"