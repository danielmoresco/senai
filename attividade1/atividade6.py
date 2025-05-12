# A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml 
# e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, faça
# um algoritmo para calcular quantos litros de refrigerante ele comprou.

lata = int(input("Olá, inisra a quantidade de latas 350ml que você deseja: "))
print (" ")
garrafa = int(input("Olá, inisra a quantidade de garrafas 600ml que você deseja: "))
print ("")
litro = int(input("Olá, inisra a quantidade de garrafas 2l que você deseja: "))
print ("")

coca_lata = lata * 350
coca_garrafa = garrafa * 600
coca_litro = litro * 2000

total_ml = coca_lata + coca_garrafa + coca_litro 
total_litro = total_ml / 1000

print ("Total de litros comprados: ",total_litro,"L")
print ("=============================================================================")
print ("Total em ml:",total_ml,"ml")
