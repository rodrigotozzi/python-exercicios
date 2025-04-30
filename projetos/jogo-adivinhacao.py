"""
O computador escolhe um número e o usuário tenta adivinhar.
O jogo fornece dicas "maior" ou "menor"
"""

from random import randint, random

while True:
    print("Escolha o Nível: ")
    print("Fácil 0 - 100: 1")
    print("Médio: 0 - 1.000: 2")
    print("Díficil 0 - 1.000.000: 3")

numero = randint()
print(x)