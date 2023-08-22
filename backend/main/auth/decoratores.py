from .. import jwt 
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def rol_required(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            #Verificar que el JWT sea correcto
            verify_jwt_in_request()
            #Obtenemos los claims (peticiones) que estan dentro del JWT
            claims = get_jwt()
            #Verificamos que el rol sea el utorizado
            if claims ['sub']['role'] in roles:
                return function(*args, **kwargs)
            else:
                return 'Role not allowed', 403
        return wrapper
    return decorator


# DECORADORES QUE YA TRAE POR DEFECTO EL JWT, pero los modificamos y redefinimos.
@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return {
        'usuarioId': usuario.id,
        'role': usuario.role
    }

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'id': usuario.id,
        'role': usuario.role,
        'email': usuario.email
    }