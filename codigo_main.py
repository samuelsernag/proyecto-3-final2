from clases.estudiante import Estudiante
from clases.docente import Docente
from clases.asignatura import Asignatura
from clases.matricula import Matricula

def main():

    # Crear docentes
    docente1 = Docente(
        id_usuario="D001",
        nombre="Juan Pérez",
        correo="juan.perez@uni.edu",
        especialidad="Matemáticas"
    )

    docente2 = Docente(
        id_usuario="D002",
        nombre="Ana Gómez",
        correo="ana.gomez@uni.edu",
        especialidad="Programación"
    )

    # Crear asignaturas
    asignatura1 = Asignatura(
        codigo="MAT101",
        nombre="Cálculo I",
        docente=docente1
    )

    asignatura2 = Asignatura(
        codigo="PRO201",
        nombre="Programación II",
        docente=docente2
    )

    # Crear estudiantes
    estudiante1 = Estudiante(
        id_usuario="E001",
        nombre="Carlos Ruiz",
        correo="carlos.ruiz@correo.com",
        semestre=3
    )

    estudiante2 = Estudiante(
        id_usuario="E002",
        nombre="María López",
        correo="maria.lopez@correo.com",
        semestre=2
    )

    # Realizar matrículas (implementación polimórfica)
    matricula1 = Matricula(estudiante1, asignatura1)
    matricula2 = Matricula(estudiante1, asignatura2)
    matricula3 = Matricula(estudiante2, asignatura1)

    # Mostrar información
    print("\n=== LISTADO DE ESTUDIANTES MATRICULADOS ===")
    matricula1.mostrar_informacion()
    matricula2.mostrar_informacion()
    matricula3.mostrar_informacion()

    print("\n=== INFORMACIÓN DOCENTES ===")
    print(docente1.obtener_informacion())
    print(docente2.obtener_informacion())


if __name__ == "__main__":
    main()
