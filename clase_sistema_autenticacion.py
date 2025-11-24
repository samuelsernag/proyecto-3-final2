class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def login(self, correo, contrasena):
        for usuario in self.usuarios:
            if usuario.correo == correo and usuario.contrasena == contrasena:
                return usuario
        return None
