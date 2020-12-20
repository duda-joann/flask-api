import pytest
from typing import Generator
from database_creation import create_app
from database_creation.models import Users


@pytest.fixture
def create_test_app() -> Generator:
    app = create_app.create_app('testing')

    yield app

    app.config['DB_FILE_PATH'].unlink(missing_ok=True)


@pytest.fixture
def client(app) -> Generator:
    with app.test_client() as client:

        yield client


@pytest.fixture
def sample(app):
    data = {
        'id': 1,
        'name':'AC/DC',
        'playcount': 100,
        'listeners': 100,
        'mbid': 'aaa-100-bcd-99-cde'
    }

    runner = app.test_cli_runner()
    runner.invoke(data)

@pytest.fixture
def user(client):
    user = {
        'username': 'test',
        'password': 'test12',
        'email': 'test@gmail.com'
    }

    client.post('/api/v1/auth/register', json=user)
    return user


@pytest.fixture
def token(client, user):
    response = client.post('/api/v1/auth/login', json= {
        'username': user['username'],
        'password': user['password']
    })

    return response.get_json()['token']

