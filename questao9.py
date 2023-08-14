#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
#em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias

anos= int(input("Informe sua idade(em anos):"))
mes = int(input("Quantos meses completos já se passaram desde seu último aniversário?"))
dia = int(input("Quantos dias faltam se passaram após o número de meses completos da resposta anteriror?"))

df = (anos * 365) + (mes * 30) + dia

print(f"Parece que você está vivo há {df} dias! Guerreiro ein?")




