
normal = float(input(" Digite quantas horas normais você trabalhou no mês: "))
print ("")
extra = float(input(" Digite quantas horas extras você trabalhou no mês: "))
print ("=============================================================================")

salario_bruto = normal * 10
horas_extras = extra * 15
total = salario_bruto + horas_extras
impostos = salario_bruto * 0.10
salario = salario_bruto - impostos
salario_liquido = salario + horas_extras




print (" valor de seu salario bruto: ",salario_bruto)
print ("=============================================================================")
print (" valor de suas horas extras: ",horas_extras)
print ("=============================================================================")
print (" total do seu salario com as horas extras: ",total)
print ("=============================================================================")
print (" valor dos impostos: ",impostos)
print ("=============================================================================")
print (" o valor total do seu salario com os impostos descontados: ",salario_liquido)


