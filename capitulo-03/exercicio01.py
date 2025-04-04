# Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
#maiores que 0.

numero = 1
contador = 0

print("Os cinco primeiros múltiplos de 3 são:")
while contador <= 4:
    if numero%3 == 0:
        print(numero)
        contador+=1
        numero+=1
    else:
        numero+=1
