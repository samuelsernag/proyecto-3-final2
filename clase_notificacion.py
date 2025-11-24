class Notificacion:
    def __init__(self, mensaje, estudiante):
        self.mensaje = mensaje
        self.estudiante = estudiante
        self.leida = False

    def marcar_como_leida(self):
        self.leida = True
