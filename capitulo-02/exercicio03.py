#Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

numero = int(input("Digite seu número: "))

if numero == 0:
    print("O número digitado foi ZERO")
elif numero%2 == 0:
    print("O número digitado foi:", numero, "e ele é PAR")
else:
    print("O número digitado foi:", numero, "e ele é IMPAR")
