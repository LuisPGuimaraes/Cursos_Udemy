lista_0 = ["Luis", "Beatriz"]
lista_1 = ["Aline", "Eder", "Duda", "Rafa", "Maria Teresa"]
lista_2 = []

i  = 0

while i < len(lista_0):
    lista_2.append(lista_0[i])
    i = i + 1

j = 0

while j < len(lista_1):
    lista_2.append(lista_1[j])
    j = j + 1

print(lista_2)
print(len(lista_2))