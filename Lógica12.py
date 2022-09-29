'''12. Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas, calcular e
escrever o seu salário total, que corresponde ao salário fixo + valor da comissão de
vendas. Caso o total de vendas ultrapasse R$ 20.000,00, exibir a mensagem "Atingiu a
Meta" e acrescente um bônus de R$ 600,00 ao salário Total'''

salFixo = float(input("Entre com o seu salário fixo: "))
valVenda = float(input("Entre com o valor das vendas efetuadas: "))
comissao = float(3*valVenda)/100

salTotal = float(salFixo + comissao)

if (valVenda > 20000):
    print("\nAtingiu a meta! Parabéns.")
    salTotal= salTotal + 600

    
print(f"Seu salário total é: {salTotal}")
