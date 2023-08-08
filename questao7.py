#A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
#pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
#prestações.

valor = float(input("Qual é o valor da compra?"))
prest = int(input("Em quantas prestações você quer pagar?"))

final = valor / prest

print(f"Cada uma das {prest:.0f} prestações terá o valor de R${final:.2f}.")