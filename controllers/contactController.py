from db import conectar
from models import Contacto, Pertenece


def seleccionarContacto(id_usuario,campo,orden):
    
    try:
        session = conectar()
        if campo == "ID" and orden == "ASC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
                        contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all()
        elif campo == "NOMBRE" and orden == "ASC":
              contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()
        elif campo == "NOMBRE" and orden == "DESC":
              contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()
    except Exception as e:
        print(e)
    finally:
        session.close()
    return contactos