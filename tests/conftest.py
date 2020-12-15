import pytest
from database_creation import create_app


@pytest.fixture
def create_test_app():
    app = create_app.create_app('testing')
    create_app.create_database()

    yield app

    app.config['DB_FILE_PATH'].unlink(missing_ok=True)


@pytest.fixture
def client(app):
    with app.test_client() as client:

        yield client


@pytest.fixture
def create_test_db():
    db = create_app.create_database()

    yield db


@pytest.fixture
def sample(data, db):
    data = {
        'id': 1,
        'name':'AC/DC',
        'playcount': 100,
        'listeners': 100,
        'mbid': 'aaa-100-bcd-99-cde'
    }

    db.session.add(data)
    db.session.commit()

