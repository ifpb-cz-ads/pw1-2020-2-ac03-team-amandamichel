# 7) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.

consumo = float(input('Informe o consumo em kWh: \n'))

print('\nTipos de instalação:\nInforme R para residências\nInforme I para indústrias\nInforme C para comércios')

tipoInstalacao = input('\nInforme o tipo de instalação: \n').upper()

if tipoInstalacao == 'R':
  if consumo <= 500:
    valorFinal = consumo * 0.40
  else:
    valorFinal = consumo * 0.65
elif tipoInstalacao == 'I':
  if consumo <= 5000:
    valorFinal = consumo * 0.55
  else:
    valorFinal = consumo * 0.60
elif tipoInstalacao == 'C':
  if consumo <= 1000:
    valorFinal = consumo * 0.55
  else:
    valorFinal = consumo * 0.60
else:
  print('\nTipo de instalação inválida')

print(f'\nO preço a pagar pelo fornecimento de energia elétrica é de R$ {valorFinal}')





