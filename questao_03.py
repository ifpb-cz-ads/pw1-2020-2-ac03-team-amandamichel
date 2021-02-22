#3) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Informe o salário do funcionário: \nR$ "))

if salario > 1250:
  aumento = salario * 0.10
else:
  aumento = salario * 0.15

salarioFinal = salario + aumento

print(f'\nValor do aumento: R$ {aumento}\nValor do salário com aumento: R$ {salarioFinal}\n')