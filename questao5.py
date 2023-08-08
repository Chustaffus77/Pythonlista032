#Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
#números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
#multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
#do primeiro pelo segundo número

v1 = float(input("Insira um número:"))
v2 = float(input("Insira mais um:"))

soma = v1 + v2
sub1 = v1 - v2
sub2 = v2 - v1
mult = v1 * v2
div = v1 / v2
res = v2 % v1

print(f"Soma:{soma}")
print(f"Subtração do 1nº pelo 2nº:{sub1}")
print(f"Subtração do 2nº pelo 1nº:{sub2}")
print(f"Multiplicação:{mult}")
print(f"Divisão:{div}")
print(f"Resto da divisão do 2º pelo 1º:{res}")
