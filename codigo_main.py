# ===============================
#       CLASES DEL SISTEMA
# ===============================

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena


class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.cursos = []
        self.notificaciones = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def recibir_notificacion(self, notificacion):
        self.notificaciones.append(notificacion)


class Docente(Usuario):
    def __init__(self, id_usuario, nombre, correo, contrasena):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.cursos_asignados = []

    def asignar_curso(self, curso):
        self.cursos_asignados.append(curso)


class Administrador(Usuario):
    pass


class Materia:
    def __init__(self, id_materia, nombre):
        self.id_materia = id_materia
        self.nombre = nombre


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


class Nota:
    def __init__(self, estudiante, curso, valor):
        self.estudiante = estudiante
        self.curso = curso
        self.valor = valor


class Notificacion:
    def __init__(self, mensaje, estudiante):
        self.mensaje = mensaje
        self.estudiante = estudiante
        self.leida = False


class CalendarioAcademico:
    def __init__(self):
        self.actividades = []


class Actividad:
    def __init__(self, nombre, fecha, descripcion):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion


class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def login(self, correo, contrasena):
        for u in self.usuarios:
            if u.correo == correo and u.contrasena == contrasena:
                return u
        return None


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

# ============================================================
#               SISTEMA FUNCIONAL (MENÚ)
# ============================================================

auth = SistemaAutenticacion()
gestor = GestorAcademico()


def registrar_estudiante():
    print("\n--- Registrar Estudiante ---")
    id_u = len(gestor.usuarios) + 1
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    est = Estudiante(id_u, nombre, correo, contrasena)
    gestor.agregar_usuario(est)
    auth.registrar_usuario(est)

    print("Estudiante registrado con éxito.\n")


def registrar_docente():
    print("\n--- Registrar Docente ---")
    id_u = len(gestor.usuarios) + 1
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")

    doc = Docente(id_u, nombre, correo, contrasena)
    gestor.agregar_usuario(doc)
    auth.registrar_usuario(doc)

    print("Docente registrado con éxito.\n")


def crear_materia():
    print("\n--- Crear Materia ---")
    id_m = len(gestor.materias) + 1
    nombre = input("Nombre de la materia: ")

    m = Materia(id_m, nombre)
    gestor.crear_materia(m)

    print("Materia creada.\n")


def crear_curso():
    print("\n--- Crear Curso ---")
    if not gestor.materias:
        print("No hay materias registradas.\n")
        return

    if not any(isinstance(u, Docente) for u in gestor.usuarios):
        print("No hay docentes registrados.\n")
        return

    print("Materias disponibles:")
    for m in gestor.materias:
        print(f"{m.id_materia}. {m.nombre}")

    id_materia = int(input("Seleccione materia: "))
    materia = next((m for m in gestor.materias if m.id_materia == id_materia), None)

    docentes = [u for u in gestor.usuarios if isinstance(u, Docente)]
    print("\nDocentes disponibles:")
    for d in docentes:
        print(f"{d.id_usuario}. {d.nombre}")

    id_doc = int(input("Seleccione docente: "))
    docente = next((d for d in docentes if d.id_usuario == id_doc), None)

    id_curso = len(gestor.cursos) + 1
    curso = Curso(id_curso, materia, docente)
    gestor.crear_curso(curso)
    docente.asignar_curso(curso)

    print("Curso creado.\n")


def inscribir_estudiante_en_curso():
    print("\n--- Inscribir Estudiante en Curso ---")

    estudiantes = [u for u in gestor.usuarios if isinstance(u, Estudiante)]
    cursos = gestor.cursos

    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    if not cursos:
        print("No hay cursos.\n")
        return

    print("Estudiantes:")
    for e in estudiantes:
        print(f"{e.id_usuario}. {e.nombre}")

    id_est = int(input("Seleccione estudiante: "))
    estudiante = next(e for e in estudiantes if e.id_usuario == id_est)

    print("\nCursos disponibles:")
    for c in cursos:
        print(f"{c.id_curso}. {c.materia.nombre} - Prof: {c.docente.nombre}")

    id_c = int(input("Seleccione curso: "))
    curso = next(c for c in cursos if c.id_curso == id_c)

    curso.agregar_estudiante(estudiante)
    estudiante.agregar_curso(curso)

    print("Estudiante inscrito exitosamente.\n")


def registrar_nota():
    print("\n--- Registrar Nota ---")

    cursos = gestor.cursos
    if not cursos:
        print("No hay cursos.\n")
        return

    for c in cursos:
        print(f"{c.id_curso}. {c.materia.nombre} - Docente: {c.docente.nombre}")

    id_curso = int(input("Seleccione curso: "))
    curso = next(c for c in cursos if c.id_curso == id_curso)

    print("\nEstudiantes:")
    for e in curso.estudiantes:
        print(f"{e.id_usuario}. {e.nombre}")

    id_est = int(input("Seleccione estudiante: "))
    estudiante = next(e for e in curso.estudiantes if e.id_usuario == id_est)

    valor = float(input("Ingrese nota: "))

    nota = Nota(estudiante, curso, valor)
    curso.registrar_nota(nota)
    gestor.generar_notificacion_si_esta_bajo(nota)

    print("Nota registrada.\n")


def ver_notificaciones():
    print("\n--- Consultar Notificaciones ---")

    estudiantes = [u for u in gestor.usuarios if isinstance(u, Estudiante)]

    for e in estudiantes:
        print(f"{e.id_usuario}. {e.nombre}")

    id_est = int(input("Seleccione estudiante: "))
    estudiante = next(e for e in estudiantes if e.id_usuario == id_est)

    print("\nNotificaciones:")
    if not estudiante.notificaciones:
        print("No tienes notificaciones.\n")
    else:
        for n in estudiante.notificaciones:
            print(f"- {n.mensaje}")
    print()


# ============================
#           MENÚ
# ============================

def menu():
    while True:
        print("""
=======================================
        SISTEMA ACADÉMICO
=======================================
1. Registrar Estudiante
2. Registrar Docente
3. Crear Materia
4. Crear Curso
5. Inscribir estudiante en curso
6. Registrar nota
7. Ver notificaciones
0. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_docente()
        elif opcion == "3":
            crear_materia()
        elif opcion == "4":
            crear_curso()
        elif opcion == "5":
            inscribir_estudiante_en_curso()
        elif opcion == "6":
            registrar_nota()
        elif opcion == "7":
            ver_notificaciones()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.\n")


if __name__ == '__main__':
    menu()
