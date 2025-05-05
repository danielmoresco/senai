#22.    Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário.

# Solicita um número do usuário
tabuada = float(input("Digite um número para ver a tabuada: "))

# Loop de 1 a 10 para exibir a tabuada
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")