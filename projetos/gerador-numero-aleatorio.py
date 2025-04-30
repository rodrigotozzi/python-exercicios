"""
Criar um programa que gere números aleatórios em um intervalo determinado pelo usuario
"""

from random import randrange

intervalo_menor = int(input("Informe o intervalo inferior para gerar o número: "))
intervalo_maior = int(input("Informe o intervalo maior para gerar o número: "))

print(randrange(intervalo_menor, intervalo_maior))