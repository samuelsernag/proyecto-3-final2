from usuario import Usuario

class Profesor(Usuario):
    def __init__(
        self,
        id: int,
        nombre: str,
        edad: int,
        sexo: str,
        documento: int,
        correo: str,
        contrasena: str,
        tipo: str,
        especialidad: str
    ):
        super().__init__(id, nombre, edad, sexo, documento, correo, contrasena, tipo)
        self.especialidad = especialidad
        self.cursos = []  # List<Curso>

    def dictarCurso(self, curso):
        self.cursos.append(curso)

    def listarCursos(self):
        return self.cursos
