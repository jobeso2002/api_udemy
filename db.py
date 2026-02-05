import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = os.getenv("DATABASE_URL")

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    if session:
        print("Conexion a base de datos ok")
    else:
        print("Error en conexion a base de datos")

    return session
