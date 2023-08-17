lista = ["Javascript","Python", "Java", "C#", "C", "C++"]

entrada_1 = input("Digite uma linguagem:")
entrada_2 = input("Digite uma outra linguagem:")


i = 0

while i < len(lista):
    if entrada_1 == lista[i]:
        print("Primeiro encontrado: ", entrada_1)
        break
    
    elif entrada_2 == lista[i]:
        print("Primeiro encontrado: ", entrada_2)
        break
    i = i + 1