from notificacion import Notificacion

class GestorAcademico:
    def __init__(self):
        self.usuarios = []
        self.materias = []
        self.cursos = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def crear_materia(self, materia):
        self.materias.append(materia)

    def crear_curso(self, curso):
        self.cursos.append(curso)

    def generar_notificacion_si_esta_bajo(self, nota):
        if nota.valor < 3.0:
            mensaje = f"[Alerta] Tu nota en {nota.curso.materia.nombre} es baja: {nota.valor}"
            notificacion = Notificacion(mensaje, nota.estudiante)
            nota.estudiante.recibir_notificacion(notificacion)
