# Faça um algoritmo que calcule e mostre a área de um losango.
# Sabe-se que: A = (diagonal_maior * diagonal_menor)/2;

#Inserção
diagonal_menor = float(input("Digite a diagonal menor : "))
diagonal_maior = float(input("Digite a diagonal maior : "))


#calculo
area = (diagonal_menor + diagonal_maior)/2 

#imprimi
print("A área do losango é : ",area)

