class Curso:
    def __init__(self, nombre: str, codigo: str, creditos: int):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.profesor = None
        self.notas = []        # List<NotaCurso>
        self.estudiantes = []  # List<Estudiante>

    def asignarProfesor(self, profesor):
        self.profesor = profesor

    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def registrarNota(self, nota):
        self.notas.append(nota)

    def calcularPromedio(self) -> float:
        pass
