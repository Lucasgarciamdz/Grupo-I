from flask_jwt_extended import verify_jwt_in_request, get_jwt

from .. import jwt


def role_required(roles):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['rol'] in roles:
                return fn(*args, **kwargs)
            else:
                return 'Rol sin permisos de acceso al recurso', 403

        return wrapper

    return decorator


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario.id_usuario


@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'rol': usuario.rol,
        'id': usuario.id_usuario,
        'email': usuario.email
    }
    return claims
