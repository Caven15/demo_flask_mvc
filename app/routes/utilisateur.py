from app import app

from app.controllers import utilisateur_controller


@app.route('/api/utilisateurs', methods=['GET'])
def get_all():
    return utilisateur_controller.get_all()