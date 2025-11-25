class Notificacion:
    def __init__(self, idNotificacion: int, mensaje: str, fechaEnvio, usuario):
        self.idNotificacion = idNotificacion
        self.mensaje = mensaje
        self.fechaEnvio = fechaEnvio
        self.leida = False
        self.usuario = usuario

    def enviar(self):
        pass

    def marcarComoLeida(self):
        self.leida = True

    def mostrar(self):
        pass
