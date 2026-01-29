from flask import Flask, jsonify, request, session
from flask import Blueprint
from models import Usuario


from db import conectar

user_api = Blueprint('user_api', __name__)

@user_api.route('/usuario', methods=['Get'])
def usuario():
    try:
        session = conectar()
        usuarios = session.query(Usuario).all()
        print(usuarios)
    except Exception as e:
        print(e)
    finally:
        session.close()
    
    return "consulta correcta usuario"        

