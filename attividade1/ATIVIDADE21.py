# Faça um algoritmo que receba o valor do salário mínimo e o valor do salário de um funcionário,(R$ 1.518 )
# calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

#Inserção
salario_minimo = float(input("Digite o salario minimo (R$ 1.518 (2025) ) : "))
salario_funcionario = float(input("Digite o seu salario: "))


#calculo
qtd_minimos = (salario_funcionario / salario_minimo)

#imprimi
print(f"A quantidade de salarios minimos que voce ganha é: {qtd_minimos:.2f}")
