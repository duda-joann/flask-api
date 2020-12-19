import pytest
from typing import Generator
from database_creation import create_app


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
def sample(app,db):
    data = {
        'id': 1,
        'name':'AC/DC',
        'playcount': 100,
        'listeners': 100,
        'mbid': 'aaa-100-bcd-99-cde'
    }

    runner = app.test_cli_runner()
    runner.invoke(data)



    

