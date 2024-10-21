from functools import wraps
from flask_jwt_extended import get_jwt
from flask import jsonify

def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims.get('role') not in roles:
                return jsonify(msg="Unauthorized"), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper