class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def actualizar_datos(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
