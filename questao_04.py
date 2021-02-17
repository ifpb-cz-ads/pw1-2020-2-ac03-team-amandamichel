#4) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até
#de 200 km, e R$ 0,45 para viagens mais longas.

km = float(input("Informe a distante em KM: "))

if km <= 200:
    print("O valor da viagem eh: ", km * 0.5)
else:
    print("O valor da viagem eh: ", km * 0.45)
