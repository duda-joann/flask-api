from flask_restful import abort
from flask import abort, jsonify
from flask_marshmallow import Marshmallow
from webargs.flaskparser import use_args
from database_creation.models import Users, user_schema
from database_creation.app import db
from .blueprint import auth_bp
from creating_api.app import app

ma = Marshmallow(app)

@auth_bp.route('register, methods ='['POST'])
@use_args(user_schema, error_status_code = 400)
def register(args: dict) -> dict:
    """
    creating/register new user
    :param args:  parameters provide by user
    :return:  return Dict
    """
    if Users.query.filter(Users.username ==args['username']).first():
            abort(409, description=f'User with username {args["username"]} existst.')

    if Users.query.filter(Users.email ==args['email']).first():
            abort(409, description=f'Mail {args["email"]} exists.')

    args['password'] = Users.generate_hashed_password('password')

    user = Users(**args)
    db.session.add(user)
    db.session.commit()

    token = user.generate_jwt().decode()

    return jsonify({'success': 'True',
                    'token': token}), 201


@auth_bp.route('/login', methods=['POST'])
@use_args(user_schema(only=['username', 'password']), error_status_code=400)
def login(args: dict) -> dict:
    """
    creating login
    :param args: dictionary, user data,
    :return: token
    """
    user = Users.query.filter(Users.username == args['username']).first()
    if not user:
        abort(401, description='Invalid credentials')

    if not user.is_password_valid(args['password']):
        abort(401, description='Invalid credentials')

    token = user.generate_jwt()

    return jsonify(token), 201


@auth_bp.route('/get-active-user', methods=['GET'])
def get_current_user(user_id: int) -> dict:
    """
    Get information about current user
    :param user_id:
    :return:
    """
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')

    return jsonify({
        'success': True,
        'data': user_schema.dump(user)
    })


@auth_bp.route('/update/password', methods=['PUT'])
@use_args(error_status_code=400)
def update_user_password(user_id: int, args: dict)-> dict:
    """
    update user password
    :param user_id: user id
    :param args:  user data
    :return: response
    """
    user = Users.query.get_or_404(user_id, description=f'User {user_id} not found')

    if not user.is_password_valid(args['current_password']):
        abort(401, description='Invalid password')

    user.password = user.generate_hashed_password(args['new_password'])
    db.session.commit()

    return jsonify({
        'success': True,
        'data': user_schema.dump(user)
    })


@auth_bp.route('/update/data', methods=['PUT'])
@use_args(user_schema(only=['username', 'email']), error_status_code=400)
def update_user_data(user_id: int, args: dict) -> dict:

    """
    update user information
    """

    if Users.query.filter(Users.username == args['username']).first():
        abort(
            409, description=f'User with username {args["username"]} already exists'
        )
    if Users.query.filter(Users.email == args['email']).first():
        abort(
            409, description=f'User with email {args["email"]} already exists'
        )

    user = Users.query.get_or_404(user_id,
                                  description=f'User with id {user_id} not found'
                                  )

    user.username = args['username']
    user.email = args['email']
    db.session.commit()

    return jsonify({
        'success': True,
        'data': user_schema.dump(user)
    })


@auth_bp.route('/delete/data', methods=['DELETE'])
@use_args(user_schema, error_status_code=400)
def delete(user_id: id):
    user = Users.query.get_or_404(user_id, description=f'User with name {user_id} not found')
    Users.delete(user)
    db.execute()
    db.commit()

    return jsonify({
        'success': True,
        'status_code': 404,
        'message': 'Bye, bye beautiful! Hasta La Vista!'
    })
