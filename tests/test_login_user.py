import allure
import requests
from conftest import create_and_delete_user
from data import APILinks
from helpers import create_user_login


class TestLoginUser:
    @allure.title('Успешная авторизация пользователя')
    def test_user_login_success(self, create_and_delete_user):
        r = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=create_and_delete_user[2])
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Ошибка при авторизации с неверным логином и паролем')
    def test_user_login_incorrect_login_data_fail(self, create_and_delete_user):
        payload = create_user_login()
        r = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)
        assert r.status_code == 401 and r.json()['message'] == "email or password are incorrect"
