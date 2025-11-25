class Universidad:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.facultades = []  # List<Facultad>

    def agregarFacultad(self, facultad):
        self.facultades.append(facultad)

    def obtenerFacultades(self):
        return self.facultades

