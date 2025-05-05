#  Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
#  Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas,
#  calcule e mostre a comissão e o salário final do funcionário.

#Inserção
salario = float(input("Digite Seu Salario : "))
vendas = float(input("Digite Valor De Suas Vendas : "))

#calculo
comissao = (vendas * 0.04)
salario_final = salario + comissao

#imprimi
print("Seu salario é : ",salario_final)



