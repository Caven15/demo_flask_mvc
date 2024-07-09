from flask import request, jsonify
from app.models.dto.utilisateur_schema import UtilisateurRegisterSchema
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.db.db_model import Utilisateur

from app.services.jwt_manager import generate_jwt
from app.services.session_scope import session_scope

def login():
    utilisateur_schema = UtilisateurRegisterSchema()
    errors = utilisateur_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400

    username = request.json['username']
    password = request.json['password']
    
    with session_scope() as session:
        utilisateur = session.query(Utilisateur).filter_by(username=username).first()
        if utilisateur and check_password_hash(utilisateur.password, password):
            access_token = generate_jwt(utilisateur,None,2)
            return jsonify(access_token), 200
        else: 
            return jsonify({'message' : 'Nom d\'utilisateur ou le mot de passe incorrect'}), 401

def register():
    # Valider les données d"ntrée avec Marshmallow
    utilisateur_register_schema = UtilisateurRegisterSchema()
    errors = utilisateur_register_schema.validate(request.json)
    if errors:
        return jsonify({'message': f'{errors}'}), 400
    # récupérer les donnée de ma requette
    username = request.json['username']
    password = request.json['password']
    
    # Sécurisation du password
    hashed_password = generate_password_hash(password)
    
    #envoyer en db
    with session_scope() as session:
        utilisateur_existant = session.query(Utilisateur).filter_by(username=username).first()
        # je vérifie si l'utilisateur n'existe pas encore en db
        if utilisateur_existant:
            return jsonify({'message': 'Cet utilisareur existe déjà !'}), 400
        
        # Créer un nouvel utilistaeur avec le mot de passe haché
        new_user = Utilisateur(username=username, password=hashed_password)
        session.add(new_user)
    return jsonify({'message': f'{username} enregistré avec succès !'}), 201