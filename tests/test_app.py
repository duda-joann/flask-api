import pytest
import requests
import tempfile
from creating_api.app import app


url = 'http://127.0.0.5000'

@pytest.fixture()


def test_render_main():
    result = requests.get(url+'/')
    assert result.status_code == 200


def test_api_artistapidata():
    result = requests.get(url + '/api/v1/artist/1')
    assert result.status_code == 200

def test_api_all_artists():
    result = requests.get(url+'def test_api')
    assert result.status_code == 200