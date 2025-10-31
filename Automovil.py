
class Automovil:
    #motor
    #potencia
    #marca
    #modelo
    #costo
    def __init__(self, mo,pot,mar, mod,co):
        self.motor = mo
        self.potencia = pot
        self.marca = mar
        self.modelo = mod
        self.costo = co

    def __str__(self):
        return (f"Motor: {self.motor}\nPotencia: {self.potencia}\n{self.marca}\n{self.modelo}")

    def manejar(self):
        print("El auto esta en movimiento, rrrrr, rrrr")


    def frenar(self):
        print("auto frenandoo")

