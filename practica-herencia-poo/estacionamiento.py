class Estancia:
    """Tiene placa y horas, cobra $20 por hora y genera un ticket con el
    formato Placa (horas h): $cobro.
    Reto: con 0 horas o menos lanza ValueError."""

    TARIFA_HORA = 20 

    def __init__(self, placa, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")
        self.placa = placa
        self.horas = horas

    def cobrar(self):
        return self.horas * self.TARIFA_HORA

    def ticket(self):
        return f"{self.placa} ({self.horas} h): ${self.cobrar():,.2f}"


class EstanciaPension(Estancia):
    """Una pensión diaria: dura siempre 24 horas y tiene tarifa fija de $250."""

    def __init__(self, placa):
        super().__init__(placa, horas=24)

    def cobrar(self):
        return 250


class EstanciaNocturna(Estancia):
    """Cobra lo mismo que una estancia normal más un cargo fijo de $50."""

    def cobrar(self):
        return super().cobrar() + 50


estancias = [
    Estancia("ABC-123", 3),
    EstanciaPension("XYZ-789"),
    EstanciaNocturna("JKL-456", 5),
]
for estancia in estancias:
    print(estancia.ticket())

Estancia("MNO-111", 0)  
