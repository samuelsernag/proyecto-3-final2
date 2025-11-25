class Usuario:
    def __init__(
        self, 
        id: int, 
        nombre: str, 
        edad: int, 
        sexo: str,
        documento: int,
        correo: str,
        contrasena: str,
        tipo: str
    ):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.documento = documento
        self.correo = correo
        self.contrasena = contrasena
        self.tipo = tipo
        self.notificaciones = []  # List<Notificacion>

    def mostrarPerfil(self):
        pass

    def iniciarSesion(self, correo, contrasena) -> bool:
        pass

    def cerrarSesion(self):
        pass

    def actualizarDatos(self, nombre, correo):
        pass
