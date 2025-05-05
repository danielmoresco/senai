#A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé direito do frango
#há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar 
#o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50,faça um 
#algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.

frangos = int(input("Olá, digite a quantidade de frangos: "))
print ("=============================================================================")

anel_chip = frangos * 4.50
anel_alimentos = frangos * (3.50 * 2)
total = anel_alimentos + anel_chip

print ("O total gasto para marcar todos os frangos são de: ",total)



