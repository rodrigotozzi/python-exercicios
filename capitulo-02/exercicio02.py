# Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
# a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
# número é inválido.

numero = int(input("Digite um número maior que zero: "))

if numero >= 0:
    print("O número digitado foi:", numero, "e sua raiz quadrada é:", (numero**2))
else:
    print("Número inválido")

