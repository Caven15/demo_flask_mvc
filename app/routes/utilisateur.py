from flask_jwt_extended import jwt_required
from app import app

from app.controllers import utilisateur_controller


@app.route('/api/utilisateurs', methods=['GET'])
@jwt_required()
def get_all():
    return utilisateur_controller.get_all()