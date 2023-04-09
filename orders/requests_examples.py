import requests


def register_buyer():
        json = {'first_name': 'Petr',
                'last_name': 'Petrov',
                'email': 's1@bk.ru',
                'password': '123@qwer',
                'company': 'google',
                'position': 'chief'}

        response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
        print('1. Регистрация пользователя')
        print(response.status_code)
        print(response.text)

        json = {'first_name': 'Ivan',
                'last_name': 'Ivanov',
                'email': 's2@bk.ru',
                'password': '123@qwer',
                'company': 'ShopWar',
                'position': 'chief',}

        response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
        print('1. Регистрация пользователя')
        print(response.status_code)
        print(response.text)


def user_login():
        json = {'email': 's1@bk.ru',
                'password': '123@qwer',
                }

        response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
        print('1. Авторизация пользователя')
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    register_buyer()
    # register_shop()
    user_login()
