'''14. Faça um programa para ler: quantidade atual em estoque, quantidade máxima em estoque
e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média
((quantidade média = quantidade máxima + quantidade mínima) /2). Se a quantidade em
estoque for maior ou igual à quantidade média, escrever a mensagem 'Não efetuar compra',
senão escrever a mensagem 'Efetuar compra'''

estoqueAt = int(input("Insira a quantidade atual em estoque de produtos: "))
estoqueMx = int(input("Insira a quantidade máxima de produtos em estoque: "))
estoqueMi = int(input("Insira a quantidade mínima de produtos em estoque: "))

media = float((estoqueMx + estoqueMi)/2)

if (estoqueAt>=media):
    print("\nNão efetuar compra!")
else:
    print("\nEfetuar compra!")
