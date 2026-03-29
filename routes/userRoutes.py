from flask import Blueprint, jsonify, request
import controllers.userController as userController

user_api = Blueprint('user_api', __name__)

@user_api.route('/usuario', methods=['GET'])
def getUsuario():
    email = request.args.get('email')
    password = request.args.get('password')

    result = userController.seleccionarUsuario(email, password)

    return jsonify({'id_usuario': result})
