# Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
#maiores que 0.

numero_usuario = int(input("Digite seu número: "))
numeros = []

if numero_usuario >= 0:
    for i in range(4):
        numeros.append(numero_usuario++1)
else:
    print("Número menor que ZERO")

print(numeros)
