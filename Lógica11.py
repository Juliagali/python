'''11. A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar 
mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um 
acréscimo de 50%. Escreva um programa Python que leia o número de horas trabalhadas 
em uma semana, o salário por hora e escreva o salário total do funcionário, que deverá ser 
acrescido das horas extras, caso tenham sido realizadas.
'''


horas_trabalhadas = int(input("Quantas horas você trabalhou essa semana? "))
salario_por_hora = float(input("Qual o seu salário por hora trabalhada? "))
salario_semanal = 0

if horas_trabalhadas <= 40:
    salario_semanal = horas_trabalhadas * salario_por_hora
    print(f"Seu pagamento essa semana foi de R${salario_semanal}")
else:
    salario_semanal = horas_trabalhadas * (salario_por_hora * 1.5)
    print(f"Seu pagamento essa semana foi de R${salario_semanal}")
