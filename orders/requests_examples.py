import requests


def register_buyer():
        json = {'first_name': 'Bruce',
                'last_name': 'Lee',
                'email': 'michman@bk.ru',
                'password': '123@qwer',
                'company': 'google',
                'position': 'chief'}

        response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
        print('1. Регистрация пользователя')
        print(response.status_code)
        print(response.text)


def register_shop():
        json = {'first_name': 'Ivan',
                'last_name': 'Ivanov',
                'email': 'ss@bk.ru',
                'password': '123@qwer',
                'company': 'ShopWar',
                'position': 'chief',
                'type': 'shop'}

        response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
        print('1. Регистрация пользователя')
        print(response.status_code)
        print(response.text)

if __name__ == '__main__':
    # register_buyer()
    # register_shop()
