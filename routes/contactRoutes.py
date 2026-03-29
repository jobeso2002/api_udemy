from flask import Blueprint, jsonify, request
import controllers.contactController as contactController

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/contactos', methods=['GET'])
def getContactos():
    id_usuario = request.args.get('id_usuario')
    campo = request.args.get('campo')
    orden = request.args.get('orden')

    contactos = contactController.seleccionar_Contactos(id_usuario, campo, orden)
    return jsonify(contactos)

@contact_api.route('/contacto', methods=['GET'])
def getContacto():
    id_contacto = request.args.get('id_contacto')
    contacto = contactController.seleccionar_Contacto(id_contacto)
    return jsonify(contacto)

@contact_api.route('/contactoStr', methods=['GET'])
def getContactoStr():
    id_usuario = request.args.get('id_usuario')
    value = request.args.get('value')

    contactos = contactController.busqueda_contactos(id_usuario, value)
    return jsonify(contactos)

@contact_api.route('/contacto', methods=['POST'])
def insertContacto():
    id_usuario = request.args.get('id_usuario')
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    direccion = request.args.get('direccion')
    email = request.args.get('email')
    telefono = request.args.get('telefono')

    result = contactController.insertar_Contacto(
        id_usuario, nombre, apellidos, direccion, email, telefono
    )

    return jsonify({'result': result})

@contact_api.route('/contacto', methods=['PUT'])
def actualizarContacto():
    id = request.args.get('id')
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    direccion = request.args.get('direccion')
    email = request.args.get('email')
    telefono = request.args.get('telefono')

    result = contactController.actualizar_Contacto(
        id, nombre, apellidos, direccion, email, telefono
    )

    return jsonify({'result': result})

@contact_api.route('/contacto', methods=['DELETE'])
def deleteContacto():
    id_usuario = request.args.get('id_usuario')
    id_contacto = request.args.get('id_contacto')

    result = contactController.eliminar_Contacto(id_usuario, id_contacto)

    return jsonify({'result': result})
