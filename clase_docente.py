from usuario import Usuario

class Docente(Usuario):
    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.cursos_asignados = []

    def asignar_curso(self, curso):
        self.cursos_asignados.append(curso)
