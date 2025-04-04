# Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("Os números digitados foram:", numero1, "e ", numero2 )
    print("O maior entre eles é:", numero1)
else:
    print("Os números digitados foram:", numero1, "e ", numero2)
    print("O maior número é:", numero2)

