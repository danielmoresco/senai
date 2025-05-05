# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a)  a idade dessa pessoa em anos;
# b)  a idade dessa pessoa em meses;
# c)  a idade dessa pessoa em dias;
# d)  a idade dessa pessoa em semanas.

#Inserção

idade = float(input("Digite seu ano de nascimento: "))
ano_atual = float(input("Digite o ano atual: "))


#calculo
ano =       (ano_atual - idade )
meses =     (ano * 12)
dias =      (ano * 365)
semanas =   (dias / 7)

#imprimi
print(f"A quantidade de anos que voce tem    é: {ano:.0f}")
print(f"A quantidade de meses que voce tem   é: {meses:.0f}")
print(f"A quantidade de dias que voce tem    é: {dias:.0f}")
print(f"A quantidade de semanas que voce tem é: {semanas:.0f}")





