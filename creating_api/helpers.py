from functools import wraps
from typing import Callable
from flask import request, abort


def token_required(function: Callable):

    """
    check if user got  required token,
    need to add checking if token is incorrect and  if token is active
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = None
        auth = request.headers.get('Authorization')
        if auth:
            token = auth.split('')[1]

        if token:
            return function(*args, **kwargs)
        else:
            abort(401, description = 'Missing token. Please login or register to get required token')

    return wrapper


