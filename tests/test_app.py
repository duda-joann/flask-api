import pytest
import requests
from flask import Flask



url = 'http://127.0.0.5000'

def test_app(app):
    assert isinstance(app, Flask)
    assert app.config['Testing ']

def test_render_main():
    result = requests.get(url+'/')
    assert result.status_code == 200


def test_api_artistapidata():
    result = requests.get(url + '/api/v1/artist/1')
    assert result.status_code == 200


def test_api_all_artists():
    result = requests.get(url+'def test_api')
    assert result.status_code == 200

