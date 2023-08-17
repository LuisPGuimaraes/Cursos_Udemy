def media_func (lista):
    soma = 0
    for i in lista:
        soma += i
    
    return soma/len(lista)

lista_teste = [1,2,3,4,5,6,7,8,9,10]
print(media_func(lista_teste))