class APILinks:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = 'api/auth/register'
    LOGIN_URL = 'api/auth/login'
    USER_URL = 'api/auth/user'
    ORDERS_URL = 'api/orders'


class UserData:
    without_name = {"email": "test@yandex.ru", "password": "test"}
    without_email = {"password": "test", "name": "test"}
    without_password = {"email": "test@yandex.ru", "name": "test"}


class IngredientsData:
    correct_ingredients = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
    incorrect_ingredients = {
        "ingredients": [
            "bdaaa6d",
            "bdaaa73"
        ]
    }
