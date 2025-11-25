class Facultad:
    def __init__(self, nombre: str, codigo: str, decano):
        self.nombre = nombre
        self.codigo = codigo
        self.programas = []  # List<Programa>
        self.decano = decano

    def agregarPrograma(self, programa):
        self.programas.append(programa)

    def obtenerProgramas(self):
        return self.programas
