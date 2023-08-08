#8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

custo = float(input("Qual é o valor do produto?"))
per = float(input("Qual é o percentual de Acréscimo?"))

acr = custo * per/100
final = custo + acr

print(f"O Valor total da venda será de R${final}0.")
