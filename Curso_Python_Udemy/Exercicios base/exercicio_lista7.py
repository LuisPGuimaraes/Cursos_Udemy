lista = [1,2,3,4,5,6,7,8,9,10,11]
print(lista)
i = 0

while i < len(lista):
    if lista[i] == 4:
        del lista[i]
    i = i + 1

print(lista)
print(len(lista)//2)
