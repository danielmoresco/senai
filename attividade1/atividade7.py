# Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um algoritmo para ler a quantidade de cada tipo de moeda,
# e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de
# um tipo, a quantidade respectiva é zero.

m1 = int(input("Digite quantas moedas de 0,01 centavos você tem: "))
print ("=============================================================================")
m2 = int(input("Digite quantas moedas de 0,05 centavos você tem: "))
print ("=============================================================================")
m3 = int(input("Digite quantas moedas de 0,10 centavos você tem: "))
print ("=============================================================================")
m4 = int(input("Digite quantas moedas de 0,25 centavos você tem: "))
print ("=============================================================================")
m5 = int(input("Digite quantas moedas de 0,50 centavos você tem: "))
print ("=============================================================================")
m6 = int(input("Digite quantas moedas de 1,00 centavos você tem: "))
print (" ")
total1 = m1 * 0.01
total2 = m2 * 0.05 
total3 = m3 * 0.10
total4 = m4 * 0.25
total5 = m5 * 0.50
total6 = m6 * 1

valor_total = ( total1 + total2 + total3 + total4 + total5 + total6 )

print (f"O pedrinho conseguiu poupar um velor de: {valor_total:.2f} R$")


