# Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente longa. Assumindo que seja possível medir sua sombra
# e a do prédio no chão, e que você lembre da sua altura, faça um algoritmo para ler os dados necessários e calcular a altura do prédio.

sombra_pessoa = float(input("Insira a altura de sua sombra em CM: "))
altura_pessoa = float(input("Insira sua altura em CM: "))
sombra_predio = float(input("Insira a altura da sombra do prédio: "))

valor = ( sombra_pessoa * sombra_predio ) / altura_pessoa
valor = valor / 100

print (f"A altura do prédio é {valor:.2f}")
