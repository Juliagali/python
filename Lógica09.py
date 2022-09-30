time = (input("Insira o nome de um time de futebol: "))
time2 = (input("Insira o nome de outro time de futebol: "))
gols1 = (input("Digite o número de gols do primeiro time: "))
gols2 = (input("Digite o número de gols do segundo time: "))



print("\nO placar do jogo é: ", time, gols1," X ",gols2, time2)
if gols1 > gols2:
    print("O time {} é o vencedor" .format(time))
if gols1 < gols2:
    print("O time {} é o vencedor" .format(time2))
    else:
         print("Empate!!")
