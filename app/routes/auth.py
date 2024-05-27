from app import app
from app.controllers import auth_controller


@app.route('/api/auth/register', methods=['POST'])
def register():
    return auth_controller.register()