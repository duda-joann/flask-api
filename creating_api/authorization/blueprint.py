from flask import Blueprint
from creating_api.authorization import auth

auth_bp = Blueprint('auth', __name__)
