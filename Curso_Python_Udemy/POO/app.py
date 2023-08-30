class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao 
    
    def ola(self,nome):
        print("Olá ", nome)



Luis = Pessoa("Luis", 21, "Back-end")
Beatriz = Pessoa("Beatriz", 21, "Front-end")

print(Luis)
print(type(Luis))
print(Luis.nome)
print(Luis.idade)
print(Luis.profissao)

Luis.ola("Luis")

