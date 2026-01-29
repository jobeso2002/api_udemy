from datetime import datetime

class Usuario():
    id: int
    nombre: str
    apellidos: str
    email: str
    password: str

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, email={self.email}, password={self.password})" 


class Contacto():
    id: str
    nombre: str
    apellidos: str
    direccion: str
    email: str
    telefono: str
    fechaCreacion: datetime

    def __repr__(self):
        return f"<Contacto(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, direccion={self.direccion}, email={self.email}, telefono={self.telefono}, fechaCreacion={self.fechaCreacion})" 
    

class Pertenece():
    id: int
    id_usuario: int
    id_contacto: int