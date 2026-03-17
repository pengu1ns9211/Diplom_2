import pytest
from helpers import *
from data import APILinks
import requests


@pytest.fixture(scope="function")
def create_and_delete_user():
    payload = create_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(APILinks.MAIN_URL + APILinks.REGISTER_URL, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(APILinks.MAIN_URL + APILinks.USER_URL, headers={'Authorization': f'{token}'})


@pytest.fixture(scope="function")
def delete_user():
    created_users = []

    def _delete_user(user_data):
        created_users.append(user_data)

    yield _delete_user

    # После теста удаляем всех созданных пользователей
    for user_data in created_users:
        login_response = requests.post(
            APILinks.MAIN_URL + APILinks.LOGIN_URL,
            data={"email": user_data['email'], "password": user_data['password']}
        )
        if login_response.status_code == 200:
            token = login_response.json()['accessToken']
            headers = {'Authorization': token}
            requests.delete(APILinks.MAIN_URL + APILinks.USER_URL, headers=headers)