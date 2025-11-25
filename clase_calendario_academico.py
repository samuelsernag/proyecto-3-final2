class CalendarioAcademico:
    def __init__(self, anio: int, semestre: int):
        self.anio = anio
        self.semestre = semestre
        self.fechasImportantes = []  # List<String>
        self.eventos = []            # List<String>

    def agregarEvento(self, evento: str):
        self.eventos.append(evento)

    def agregarFechaImportante(self, fecha: str):
        self.fechasImportantes.append(fecha)

    def mostrarCalendario(self):
        pass
