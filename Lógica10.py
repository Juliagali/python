'''10. Ler as notas de avaliação de um jogador sobre a 1ª e 2ª. fases de um Game e em seguida 
escrever uma mensagem informando se o jogador avaliou sua experiência como sendo boa 
ou regular 
Experiência boa: média das notas das fases maior ou igual a 8.0
Experiência regular: Média das notas das fases abaixo de 8.0 '''



fase1 = float(input("Insira a nota da fase 1: "))
fase2 = float(input("Insira a nota da fase 2: "))
media = float(fase1 + fase2)/2

if media >= 8:
    print("\nExperiência boa!!")
if media < 8:    
        print("\nExperiência regular")
print ("\nSua média foi: ", media)
