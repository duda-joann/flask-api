import pytest


def test_register_user(client):
    response = client.post('/api/v1/auth/register',
                           json ={
                               'username':'test',
                                'password': '123456',
                                'email': 'test@gmail.com',
                           })
    response_data = response.get_json()
    assert response.status_code == 201
    assert response.headers =='application/json'
    assert response_data['sucess'] is True
    assert response_data['token']


@pytest.mark.paramatrize(
    'data','missing_field',
    [
        ({'username': 'test', 'password': 'nie_mam_siły'}, 'email'),
    ({'username': 'test', 'email': 'niewiemcorobie@gmail.com'}, 'password'),
    ({'password': 'nie_mam_siły', 'email': 'niewiemcorobie@gmail.com'}, 'username'),
    ]
        )
def test_registration_invalid_data(client, data, missing_field):
    response = client.post('/api/v1/auth/register',
                           json=data)
    response_data = response.get_json()
    assert response.status_code == 400
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['sucess'] is False
    assert 'token' not in response_data
    assert missing_field in response_data


@pytest.mark.paramatrize(
    'data', 'repeated_name',
    [({'username':'test', 'password': '124525', 'email':'testy@gmail.com'}, 'username'),
     ({'username': 'ozzy', 'password': 'sabbathbloodysabbath', 'email: test@gmail.com'}),
     ])
def test_registration_not_available_email_or_username(client, data, missing_field):
    response = client.post('/api/v1/auth/register',
                           json=data)
    response_data = response.get_json()
    assert response.status_code == 400
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['sucess'] is False
    assert 'token' not in response_data
    assert missing_field in response_data


def test_login_register_user(client):
    response = client.post('/api/v1/auth/login',
                           json ={
                               'username':'test',
                                'password': 'test12',
                           })
    response_data = response.get_json()
    assert response.status_code == 201
    assert response.headers =='application/json'
    assert response_data['sucess'] is True
    assert response_data['token']

def test_login_nonexistent_user(client):
    response = client.post('/api/v1/auth/login',
                           json={
                               'username': 'notest',
                               'password': 'test12',
                           })
    response_data = response.get_json()
    assert response.status_code == 409
    assert response.headers == 'application/json'
    assert response_data['sucess'] is None
    assert 'token' not in response_data

def test_login_with_incorrect_password(client):
    response = client.post('/api/v1/auth/login',
                           json={
                               'username': 'test',
                               'password': 'testelllo',
                           })
    response_data = response.get_json()
    assert response.status_code == 409
    assert response.headers == 'application/json'
    assert response_data['sucess'] is None
    assert 'token' not in response_data


def test_get_current_user(client, user, token):
    response = client.get('api/v1/auth/get-active-user', token)
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['sucess'] is True
    assert response_data['data']['username']== user['username']
    assert response_data['data']['email'] == user['email']


