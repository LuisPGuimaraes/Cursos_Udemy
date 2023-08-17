def par_func (lista):
    lista_par = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
    
    return lista_par

lista_teste = [1,2,3,4,5,6,7,8,9,10]
print(par_func(lista_teste))