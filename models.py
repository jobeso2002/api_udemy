from datetime import datetime
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Usuario(Base):
    __tablename__ = 'usuario'

    id: int
    nombre: str
    apellidos: str
    email: str
    password: str

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

@dataclass
class Contacto(Base):
    __tablename__ = 'contacto'

    id: int
    nombre: str
    apellidos: str
    direccion: str
    email: str
    telefono: str
    fechaCreacion: datetime

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaCreacion = Column(DateTime, default=datetime.today)

@dataclass
class Pertenece(Base):
    __tablename__ = 'pertenece'

    id: int
    id_usuario: int
    id_contacto: int

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_contacto = Column(Integer, nullable=False)
