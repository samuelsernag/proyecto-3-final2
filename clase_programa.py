class Programa:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []  # List<Estudiante>
        self.cursos = []       # List<Curso>

    def agregarCurso(self, curso):
        self.cursos.append(curso)

    def inscribirEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def obtenerPromedios(self) -> float:
        pass
