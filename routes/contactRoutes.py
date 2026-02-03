from flask import Flask, jsonify, request
from flask import Blueprint
import controllers.contactController as contactController


contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/contactos', methods=['Get'])
def getContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    campo = parametros['campo']
    orden = parametros['orden']
    contactos = contactController.seleccionarContacto(id_usuario,campo,orden)
    return jsonify(contactos)

