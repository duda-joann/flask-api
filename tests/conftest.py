import pytest
from database_creation.create_db import create_app, create_database


@pytest.fixture
def create_test_app():
    app = create_app('testing')
    create_database()

    yield app

    app.config['DB_FILE_PATH'].unlink(missing_ok=True)
