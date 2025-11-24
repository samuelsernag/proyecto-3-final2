from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.cursos = []
        self.notificaciones = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def recibir_notificacion(self, notificacion):
        self.notificaciones.append(notificacion)
