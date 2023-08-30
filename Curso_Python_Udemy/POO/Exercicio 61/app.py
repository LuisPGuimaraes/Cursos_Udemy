class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer(self,litros):
        if self.tanque >= 100:
            print("Tanque está cheio")
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100
            print("Carro abastecido!", self.tanque, "Litros")


    def dirigir(self, km):
        km_litro = 10
        self.tanque -= km/km_litro


gol = Carro("Vw", 20000, 4, 80)

gol.dirigir(50)
print(gol.tanque)





