import requests
import json

from hasher import Hasher


class FluxAPIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url

    def get_root(self):
        url = f"{self.base_url}/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

    def get_all_users(self):
        url = f"{self.base_url}/users"
        repsponse = requests.get(url)

        if repsponse.status_code == 200:
            return repsponse.json()

    def get_user_by_id(self, id: int):
        url = f"{self.base_url}/users/{id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

    def create_user(
        self, username: str, email: str, is_admin: bool, password_hash: str
    ):
        url = f"{self.base_url}/users"

        user_data = {
            "username": username,
            "email": email,
            "is_admin": is_admin,
            "password_hash": password_hash,
        }
        response = requests.post(url, json=user_data)

        if response.status_code == 200:
            return response.json()

    def update_user(
        self,
        id: int,
        username: str = None,
        email: str = None,
        is_admin: bool = None,
        password_hash: str = None,
    ):
        url = f"{self.base_url}/users/{id}"

        user_data = {
            "username": username,
            "email": email,
            "is_admin": is_admin,
            "password_hash": password_hash,
        }
        response = requests.patch(url, json=user_data)

        if response.status_code == 200:
            return response.json()


if __name__ == "__main__":
    client = FluxAPIClient()

    # data = client.create_user(
    #     username="user",
    #     email="user@temp.com",
    #     is_admin=False,
    #     password_hash=Hasher.hash_string("user"),
    # )
    # # print(data)

    # data = client.get_user_by_id(id=1)
    data = client.update_user(id=1, username="aryose", is_admin=True)

    print(json.dumps(data, indent=4, ensure_ascii=False))
