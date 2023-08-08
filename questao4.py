 #Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
#tela o valor do índice de massa corporal desta pessoa (IMC).
#Fórmula: IMC = peso / altura2
 #- Obs: peso em quilos e altura em metros

nome = input("Qual seu nome?")
quilo = float(input(f"{nome}, iremos tirar o seu IMC agora! Quantos quilos você pesa?"))
altura = float(input("Agora por favor, a sua altura:"))
imc = quilo / (altura*altura)



print(f"Com base nos dados apresentados, seu IMC (Índice de Massa Corporal) equivale a {imc}! Espero ter ajudado!")
