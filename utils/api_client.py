import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    return requests.get(f"{BASE_URL}/users")

def create_user(name, job):
    payload = {
        "name": name,
        "job": job
    }
    return requests.post(f"{BASE_URL}/users", json=payload)