"""
O computador escolhe um número e o usuário tenta adivinhar.
O jogo fornece dicas "maior" ou "menor"
"""

from random import randint

def checa_numero(entrada):
    try:
        int(entrada)
    except ValueError:
        print("Valor Incorreto")

while True:
    print("Escolha o Nível: ")
    print("Fácil 0 - 100: 1")
    print("Médio: 0 - 1.000: 2")
    print("Díficil 0 - 1.000.000: 3")
    nivel = input()
    try:
        int(nivel)
        break
    except ValueError:
        print("Valor Incorreto")

if int(nivel) == 1:
        numero_certo = randint(0, 2)
        while True:
            chute = input("Informe o número entre 0 e 100: ")
            checa_numero(chute)
            if  0 <= int(chute) <= 100:
                if int(chute) == numero_certo:
                    print("Parabéns, vc acertou o número!")
                    break
                elif int(chute) < numero_certo:
                    print("Errado, o número certo é MAIOR")
                elif int(chute) > numero_certo:
                    print("Errado, o número certo é MENOR")
            else:
                print("Valor Inválido!")