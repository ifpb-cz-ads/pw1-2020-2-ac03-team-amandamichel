#6) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
#de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido
#pelo número de meses a pagar.

valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salario: "))
anos = int(input("Informe a quantidade de anos a pagar: "))

porcentagem = salario * 0.3
messes = anos * 12
valor_parcela = valor_casa / messes

if valor_parcela <= porcentagem:
    print("Empretimo aprovado!")
    print(messes ,"parcelas de %.2f" %valor_parcela)
else:
    print("Emprestimo recusado!")

