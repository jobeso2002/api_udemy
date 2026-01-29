from flask import Flask, jsonify, request
from flask import Blueprint


user_api = Blueprint('user_api', __name__)

@user_api.route('/usuario', methods=['Get'])
def usuario():
    return "funcionando Usuario"