#Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
#valor com o acréscimo dos 10% da gorjeta do garçom

valor = float(input("Qual é o valor da conta a ser paga?"))
gorj = 10/100 * valor
final = valor + gorj

print(f"Pelo excelente serviço do garçom, tivemos um acréscimo de {gorj} reais, totalizando assim {final}. Volte sempre!")