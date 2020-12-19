
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


def test_registration_invalid_data(clients):
    pass


