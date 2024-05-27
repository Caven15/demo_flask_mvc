
from datetime import timedelta

from flask_jwt_extended import create_access_token


def generate_jwt(utilisateur, other_claims=None, temps_valide=1):
    claims = {
        'id' : utilisateur.id,
        'username' : utilisateur.username
    }
    
    if other_claims:
        claims.update(other_claims)
    
    expire_dans = timedelta(hours=temps_valide)
    
    new_token = create_access_token(identity=str(utilisateur.id), 
                                    additional_claims=claims, 
                                    expires_delta= expire_dans)
    
    return new_token