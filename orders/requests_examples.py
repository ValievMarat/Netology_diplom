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
            'position': 'chief', }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
    print('1. Регистрация пользователя')
    print(response.status_code)
    print(response.text)


def register_shop():
    json = {'first_name': 'Fedor',
            'last_name': 'Dostoevski',
            'email': 'shop3@bk.ru',
            'password': '123@qwer',
            'company': 'shp3',
            'position': 'manager',
            'type': 'shop'}

    response = requests.post('http://127.0.0.1:8000/api/v1/user/register', json=json)
    print('1. Регистрация продавца')
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


def get_shops():
    print('Shops:')

    response = requests.get('http://127.0.0.1:8000/api/v1/shops')
    print(response.status_code)
    print(response.text)


def get_products(filter=''):
    print('Products:')

    response = requests.get('http://127.0.0.1:8000/api/v1/products' + filter)
    print(response.status_code)
    print(response.text)


def get_categories():
    print('Categories:')

    response = requests.get('http://127.0.0.1:8000/api/v1/categories')
    print(response.status_code)
    print(response.text)


def get_partner_status():
    print('Partner status:')

    # login
    json = {'email': 'shop3@bk.ru',
            'password': '123@qwer',
            }
    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/api/v1/partner/state', headers=headers)
    print(response.status_code)
    print(response.text)


def get_partner_orders():
    print('Partner status:')

    # login
    json = {'email': 'shop3@bk.ru',
            'password': '123@qwer',
            }
    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/api/v1/partner/orders', headers=headers)
    print(response.status_code)
    print(response.text)


def update_price_partner():
    # login
    json = {'email': 'shop3@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # update price
    json = {'url': 'https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml',
            }
    headers = {
        'Authorization': f'Token {token}'
    }

    response = requests.post('http://127.0.0.1:8000/api/v1/partner/update', json=json, headers=headers)
    print('1. Загрузка товаров')
    print(response.status_code)
    print(response.text)


def create_contacts():
    # login
    json = {'email': 's1@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # create_contacts
    json = {'city': 'EKB',
            'street': 'Lenina',
            'house': '12',
            'structure': '123',
            'building': '123',
            'apartment': '123',
            'phone': '+79454466565'
            }
    headers = {
        'Authorization': f'Token {token}'
    }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/contact', json=json, headers=headers)
    print('1. Создание контактов')
    print(response.status_code)
    print(response.text)


def get_contacts():
    # login
    json = {'email': 's1@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # get contacts
    headers = {
        'Authorization': f'Token {token}'
    }

    response = requests.get('http://127.0.0.1:8000/api/v1/user/contact', headers=headers)
    print('Контакты')
    print(response.status_code)
    print(response.text)


def add_goods_to_basket():
    # login
    json = {'email': 's1@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # add goods
    headers = {
        'Authorization': f'Token {token}'
    }

    json = {'items': [{'product_info': '3',
                       'quantity': '2'},
                      {'product_info': '4',
                       'quantity': '2'}
                      ],
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/basket', headers=headers, json=json)
    print('Basket')
    print(response.status_code)
    print(response.text)


def get_basket():
    # login
    json = {'email': 's1@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # add goods
    headers = {
        'Authorization': f'Token {token}'
    }

    response = requests.get('http://127.0.0.1:8000/api/v1/basket', headers=headers)
    print('Basket')
    print(response.status_code)
    print(response.text)


def create_order():
    # login
    json = {'email': 's1@bk.ru',
            'password': '123@qwer',
            }

    response = requests.post('http://127.0.0.1:8000/api/v1/user/login', json=json)
    DATA = response.json()
    token = DATA['Token']

    # create order
    headers = {
        'Authorization': f'Token {token}'
    }

    json = {'id': '1',
            'contact': '1',
            }
    response = requests.post('http://127.0.0.1:8000/api/v1/order', headers=headers, json=json)
    print('create order')
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    # register_buyer()
    # user_login()
    # create_contacts()
    # get_contacts()
    # register_shop()
    #
    # update_price_partner()
    #
    # get_shops()
    # get_products()
    # get_products('?shop_id=1')
    # get_categories()
    #
    # get_partner_status()
    # get_partner_orders()

    # add_goods_to_basket()
    # get_basket()

    # create_order()
