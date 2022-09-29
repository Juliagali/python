'''13. Faça um programa para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se
saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever
a mensagem 'Saldo Negativo'.'''

numConta = int(input("Entre com o número da sua conta bancária: "))
saldo = float(input("Entre com seu saldo atual: "))
debito = float(input("Entre com seu débito: "))
credito = float(input("Entre com o seu crédito: "))

saldoAt = float (saldo-debito+credito)

if (saldoAt >= 0):
    print("\nSaldo positivo!!")

if (saldoAt < 0):
    print("\nSaldo negativo!!")


print(f"Seu saldo atual é: {saldoAt}")
