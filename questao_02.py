#2) Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
n3 = int(input("Informe o terceiro valor: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

print("O maior valor eh: ", maior)
print("O menor valor eh: ", menor)
