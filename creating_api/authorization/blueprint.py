from flask import Blueprint
from creating_api.authorization import auth

auth_bp = Blueprint('auth', __name__, url_prefix='api/v1/auth')
