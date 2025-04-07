# Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
# lidos.

lista = []

for sequencia in range(6):
    lista.append(int(input("Digite um número inteiro: ")))

print("Os números digitados foram:")
for numero in lista:
    print(numero)
