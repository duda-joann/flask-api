import pytest
import requests
from creating_api.app import app


url = 'http://127.0.0.5000'


def test_render_main():
    result = requests.get(url+'/')
    assert result.status_code == 200

def test_api_artistapidata():
    result = requests.get(url + '/api/v1/artist/1')
    assert result.status_code == 200