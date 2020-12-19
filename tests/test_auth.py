import pytest


def test_register_user(client):
    response = client.post('/api/v1auth/register',
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
    response = client.post('/api/v1auth/register',
                           json=data)
    response_data = response.get_json()
    assert response.status_code == 400
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['sucess'] is False
    assert 'token' not in response_data
    assert missing_field in response_data



