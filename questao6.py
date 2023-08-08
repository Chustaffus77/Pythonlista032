#Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
#ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
#do mês.

fixo = float(input("Insira o seu salário fixo, por favor:"))
vend = float(input("Agora coloque o total de vendas:"))
com = 15/100 * vend
ptotal = fixo + com

print(f"O seu salário completo corresponde a singela quantia de R${total}0")

