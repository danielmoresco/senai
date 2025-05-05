#16.    Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
#a)  o novo peso se a pessoa engordar 15% sobre o peso digitado;
#b)  o novo peso se a pessoa emagrecer 20% sobre o peso digitado.


#Inserção
peso = float(input("Digite Seu Peso (EM KG) : "))


#calculo
emagrecer = peso - (peso * 0.20)
engordar = peso + (peso * 0.15)

#imprimi
print("se engordar 15% seu peso sera:",engordar)
print("se emagrecer 20% seu peso sera:",emagrecer)

