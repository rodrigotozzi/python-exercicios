"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""

lista = []
contador = 0

for i in range(1, 11):
    print("Digite o valor", i,"/ 10: ")
    lista.append(int(input()))

for i in lista:
    if i%2 == 0:
        contador += 1

if contador <= 0:
    print("Nenhum número par foi digitado")
elif contador == 1:
    print("Somente um único número par foi digitado")
else:
    print("Foram digitados", contador, "números pares")
