produto_a = ["Camisa", "Azul", 50.45]
produto_b = ["Calça", "Cinza", 110.00]
produto_c = ["Blusa", "verde", 250.00]

lista_produtos = [produto_a, produto_b, produto_c]

print(lista_produtos)

for i in lista_produtos:
    print("O produto é: %s e tem a cor %s e o seu preço é: R$%.2f" %(i[0], i[1], i[2]))