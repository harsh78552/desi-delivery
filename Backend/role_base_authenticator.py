from functools import wraps

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt


def checkRole(*role_required):
    def decorator(x):
        @wraps(x)
        @jwt_required(locations=['headers'])
        def decorated_functions(*args, **kwargs):
            authorize = get_jwt()
            if authorize['role'] not in role_required:
                return jsonify({'message': 'access denied'}), 403
            return x(*args, **kwargs)

        return decorated_functions

    return decorator
