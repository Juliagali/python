#ler e armazenar na memória dois números inteiros e em seguida, mostrar o
#menor valor caso exista#
num1 = int(input("Insira um valor inteiro: "))
num2= int(input("Insira o segundo valor inteiro: "))
resultado = 0
if (num1 < num2):
    resultado = num1
    if (num2 < num1):
        resultado=num2
else:
    print("Os números são iguais")
    


print("O menor número é", resultado)
