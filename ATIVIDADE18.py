# 18.    Faça um algoritmo que calcule e mostre a área de um trapézio. Sabe-se que: A = (base maior + base menor)* altura)/2 ; ,,0,,
#Inserção
base_menor = float(input("Digite a base menor : "))
base_maior = float(input("Digite a base maior : "))
altura = float(input("Digite a altura : "))

#calculo
area = ((base_maior + base_menor)* altura) /2 

#imprimi
print("A área do trapezio é : ",area)