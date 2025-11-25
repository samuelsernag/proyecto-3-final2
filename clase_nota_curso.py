class NotaCurso:
    def __init__(self, valor: float, fecha, tipo: str, curso, estudiante):
        self.valor = valor
        self.fecha = fecha
        self.tipo = tipo
        self.curso = curso
        self.estudiante = estudiante

    def getValor(self) -> float:
        return self.valor

    def setValor(self, valor: float):
        self.valor = valor
