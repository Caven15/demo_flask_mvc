from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models.db.db_model import Utilisateur
from app.models.dto.utilisateur_schema import UtilisateurSchema
from app.services.session_scope import session_scope


@jwt_required()
def get_all():
    with session_scope() as session:
        utilisateurs = session.query(Utilisateur).all()
        utilisateur_schema = UtilisateurSchema(many=True)
        serialized_users = utilisateur_schema.dump(utilisateurs)
    return jsonify(serialized_users), 200