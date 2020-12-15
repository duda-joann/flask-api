import requests
from flask import Flask

url = 'http://127.0.0.5000'

def test_app(app):
    assert isinstance(app, Flask)
    assert app.config['Testing ']


def test_render_main():
    result = requests.get(url+'/')
    assert result.status_code == 200



