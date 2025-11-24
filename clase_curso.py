class Curso:
    def __init__(self, id_curso, materia, docente):
        self.id_curso = id_curso
        self.materia = materia
        self.docente = docente
        self.estudiantes = []
        self.notas = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def registrar_nota(self, nota):
        self.notas.append(nota)
