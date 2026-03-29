from db import conectar
from models import Usuario

def seleccionarUsuario(email, password):
    id_usuario = 0

    try:
        session = conectar()
        usuario = session.query(Usuario).filter(
            Usuario.email == email,
            Usuario.password == password
        ).first()

        if usuario:
            id_usuario = usuario.id

    except Exception as e:
        print(e)

    finally:
        session.close()

    return id_usuario
