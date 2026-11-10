class Boleto:
    """Tiene cliente, función y precio base de $90. Sabe calcular su precio
    y generar su ticket con el formato Cliente - Función: $precio."""

    def __init__(self, cliente, funcion):
        self.cliente = cliente
        self.funcion = funcion
        self.precio_base = 90

    def calcular_precio(self):
        return self.precio_base

    def ticket(self):
        return f"{self.cliente} - {self.funcion}: ${self.calcular_precio():,.2f}"


class BoletoEstudiante(Boleto):
    """Cuesta lo mismo que un boleto normal, con un 30 % de descuento."""

    def __init__(self, cliente, funcion, descuento=0.30):
        super().__init__(cliente, funcion)
        self.descuento = descuento

    def calcular_precio(self):
        precio_normal = super().calcular_precio()
        return precio_normal - precio_normal * self.descuento


class BoletoCortesia(Boleto):
    """Siempre cuesta $0."""

    def calcular_precio(self):
        return 0


class BoletoTerceraEdad(BoletoEstudiante):
    """Reto: 50 % de descuento."""

    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion, descuento=0.50)


boletos = [
    Boleto("Andrea", "Sala 2, 18:00"),
    BoletoEstudiante("Bruno", "Sala 2, 18:00"),
    BoletoCortesia("Carla", "Sala 5, 20:30"),
]
for boleto in boletos:
    print(boleto.ticket())

print(BoletoTerceraEdad("Diana", "Sala 1, 16:00").ticket())
