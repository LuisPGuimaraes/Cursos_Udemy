class Carro:
    def __init__(self, portas, motor, teto, marca, preco):
        self.portas = portas 
        self.motor = motor 
        self.teto = teto
        self.marca = marca 
        self.preco = preco 

gol = Carro(4, 1.0, False, "VW", 21000)
meriva = Carro(4,1.6, False,"Chevrolet", 17000)
veloster = Carro(3, 2.0, True, "Hyundai", 60000)

print(gol.marca, gol.motor, gol.marca)
print(meriva.marca, meriva.portas)
print(veloster.portas, veloster.teto, veloster.preco)