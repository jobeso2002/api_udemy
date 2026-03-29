from db import conectar
from models import Contacto, Pertenece

def seleccionar_Contactos(id_usuario, campo, orden):
    try:
        session = conectar()

        query = session.query(Contacto).join(
            Pertenece, Contacto.id == Pertenece.id_contacto
        ).filter(Pertenece.id_usuario == id_usuario)

        if campo == "ID":
            if orden == "ASC":
                query = query.order_by(Contacto.id)
            else:
                query = query.order_by(Contacto.id.desc())

        elif campo == "NOMBRE":
            if orden == "ASC":
                query = query.order_by(Contacto.nombre)
            else:
                query = query.order_by(Contacto.nombre.desc())

        contactos = query.all()

        return contactos

    except Exception as e:
        print(e)
        return []

    finally:
        session.close()


def seleccionar_Contacto(id):
    try:
        session = conectar()
        contacto = session.get(Contacto, id)
        return contacto

    except Exception as e:
        print(e)
        return None

    finally:
        session.close()


def busqueda_contactos(id_usuario, value):
    try:
        session = conectar()

        contactos = (
            session.query(Contacto)
            .join(Pertenece, Contacto.id == Pertenece.id_contacto)
            .filter(Pertenece.id_usuario == id_usuario)
            .filter(
                (Contacto.nombre.ilike(f"%{value}%")) |
                (Contacto.apellidos.ilike(f"%{value}%")) |
                (Contacto.direccion.ilike(f"%{value}%")) |
                (Contacto.email.ilike(f"%{value}%"))
            )
            .order_by(Contacto.nombre)
            .all()
        )

        return contactos

    except Exception as e:
        print(e)
        return []

    finally:
        session.close()


def insertar_Contacto(id_usuario, nombre, apellidos, direccion, email, telefono):
    try:
        session = conectar()

        contacto = Contacto(
            nombre=nombre,
            apellidos=apellidos,
            direccion=direccion,
            email=email,
            telefono=telefono
        )

        session.add(contacto)
        session.commit()
        session.refresh(contacto)

        pertenece = Pertenece(
            id_usuario=id_usuario,
            id_contacto=contacto.id
        )

        session.add(pertenece)
        session.commit()

        return True

    except Exception as e:
        print(e)
        return False

    finally:
        session.close()


def actualizar_Contacto(id, nombre, apellidos, direccion, email, telefono):
    try:
        session = conectar()

        contacto = session.get(Contacto, id)

        if not contacto:
            return False

        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono

        session.commit()
        return True

    except Exception as e:
        print(e)
        return False

    finally:
        session.close()


def eliminar_Contacto(id_usuario, id_contacto):
    try:
        session = conectar()

        session.query(Pertenece).filter(
            Pertenece.id_contacto == id_contacto,
            Pertenece.id_usuario == id_usuario
        ).delete()

        contacto = session.get(Contacto, id_contacto)

        if contacto:
            session.delete(contacto)

        session.commit()
        return True

    except Exception as e:
        print(e)
        return False

    finally:
        session.close()
