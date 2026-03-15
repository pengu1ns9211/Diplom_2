import allure
import requests
from conftest import create_and_delete_user
from data import APILinks, IngredientsData


class TestCreateOrder:
    @allure.title('Успешное создание заказа авторизованным пользователем')
    def test_create_order_authorised_user_success(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        r = requests.post(APILinks.MAIN_URL + APILinks.ORDERS_URL, headers=token,
                          data=IngredientsData.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Успешное создание заказа неавторизованным пользователем')
    def test_create_order_user_without_authorisation_success(self, create_and_delete_user):
        r = requests.post(APILinks.MAIN_URL + APILinks.ORDERS_URL, data=IngredientsData.correct_ingredients)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title('Успешное создание заказа без ингредиентов')
    def test_create_order_without_ingredients_fail(self, create_and_delete_user):
        r = requests.post(APILinks.MAIN_URL + APILinks.ORDERS_URL)
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Ошибка при создании заказа c неверном хеше ингредиентов')
    def test_create_order_incorrect_hash_fail(self, create_and_delete_user):
        r = requests.post(APILinks.MAIN_URL + APILinks.ORDERS_URL, data=IngredientsData.incorrect_ingredients)
        assert r.status_code == 500 and 'Internal Server Error' in r.text
