import pytest
import allure
import requests
from conftest import create_and_delete_user
from data import APILinks, UserData
from helpers import create_user_data


class TestCreateUser:
    @allure.title('Успешная регистрация нового пользователя')
    def test_create_new_user_success(self, create_and_delete_user):
        payload = create_user_data()
        r = requests.post(APILinks.MAIN_URL + APILinks.REGISTER_URL, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Ошибка при создании пользователя с данными уже зарегистрированного пользователя ')
    def test_create_user_with_duplicate_data_fail(self, create_and_delete_user):
        r = requests.post(APILinks.MAIN_URL + APILinks.REGISTER_URL, data=create_and_delete_user[1])
        assert r.status_code == 403 and r.json()['message'] == "User already exists"

    @allure.title('Ошибка при создании пользователя без обязательных полей')
    @pytest.mark.parametrize('payload', (UserData.without_name, UserData.without_email, UserData.without_password))
    def test_create_user_without_required_fields_fail(self, payload):
        r = requests.post(APILinks.MAIN_URL + APILinks.REGISTER_URL, data=payload)
        assert r.status_code == 403 and r.json()['message'] == "Email, password and name are required fields"
