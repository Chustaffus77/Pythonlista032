#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
#em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias

anos= int(input("Quantos anos?"))
mes = int(input("Quantos meses?"))
dia = int(input("Quantos dias?"))

df = (anos * 365) + (mes * 30) + dia

print(f"Parece que você está vivo há {df} dias! Guerreiro ein?")




