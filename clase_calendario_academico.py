class CalendarioAcademico:
    def __init__(self):
        self.actividades = []
        self.fechas_importantes = []

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def agregar_fecha_importante(self, fecha):
        self.fechas_importantes.append(fecha)
