#  Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

#Inserção
cateto1 = float(input("Digite o valor primeiro cateto: "))
cateto2 = float(input("Digite o valor segundo cateto: "))


#calculo
hip = (cateto1 * cateto1) +  (cateto2 * cateto2)

#resultado 
print(f"O valor da hipontenusa é : {hip:.0f}")
