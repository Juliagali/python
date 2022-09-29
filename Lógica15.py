'''5. Escreva um programa Python que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: A - álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 7,30 e o preço do litro do
álcool é R$ 5,90.'''

litrosV = float(input("Insira o número de litros vendidos: "))
tipo = str(input("Qual é o tipo do combustível? A - álcool, G-gasolina "))

if (tipo == "A"):
    total = float(litrosV * 5.90)
if (tipo == "G"):
    total = float(litrosV * 7.30)


print(f"\nO valor a ser pago pelo cliente é: {total}")    
