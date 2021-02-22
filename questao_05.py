# 5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

numero1 = float(input('Informe o primeiro número: \n'))
numero2 = float(input('Informe o segundo número: \n'))

print('\nOperações disponíveis:\nInforme + para somar\nInforme - para subtrair\nInforme * para multiplicar\nInforme / para dividir\n')

operacao = input('Informe qual operação gostaria de calcular: ')

if operacao == '+':
  print(f'\n{numero1} + {numero2} = {numero1 + numero2}')
elif operacao == '-':
  print(f'\n{numero1} - {numero2} = {numero1 - numero2}')
elif operacao == '*':
  print(f'\n{numero1} * {numero2} = {numero1 * numero2}')
elif operacao == '/':
  print(f'\n{numero1} / {numero2} = {numero1 / numero2}')
else:
  print('\nOperação não suportada')

