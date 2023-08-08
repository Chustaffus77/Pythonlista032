#Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
#programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros

nome = input("Qual seu nome?")
quilo = float(input(f"{nome},quantos quilos você pesa?"))
altura = float(input("Agora por favor, a sua altura:"))

grama = quilo * 1000
cent = altura * 100

print(f"Com base nos dados apresentados, você mede {cent}cm de altura e pesa {grama}g")
