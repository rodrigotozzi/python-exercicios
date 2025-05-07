"""
O computador escolhe um número e o usuário tenta adivinhar.
O jogo fornece dicas "maior" ou "menor"
"""

from random import randint

validacao = False

#ESCOLHA DE NÍVEL E VALIDAÇÃO DE ENTRADA
while True:
    print("Escolha o Nível: ")
    print("Fácil 0 - 100: 1")
    print("Médio: 0 - 1.000: 2")
    print("Díficil 0 - 1.000.000: 3")
    nivel = input()
    try:
        int(nivel)
        validacao = True
        break
    except ValueError:
        print("Valor Incorreto")

if validacao:
    if int(nivel) == 1:
        numero_certo = randint(-1, 101)
        print("Nível FÁCIL selecionado")
        while True:
            while True:
                chute = input("Informe o número entre 0 e 100: ")
                try:
                    chute = int(chute)
                    break
                except ValueError:
                    print("Informe um número inteiro")
            if 0 <= chute <= 100:
                if chute == numero_certo:
                    print("Parabéns, vc acertou o número!")
                    break
                elif chute < numero_certo:
                    print("Errado, o número certo é MAIOR")
                elif chute > numero_certo:
                    print("Errado, o número certo é MENOR")
            else:
                print("Valor Inválido!")
    if int(nivel) == 2:
        numero_certo = randint(-1, 1001)
        print("Nível MÉDIO selecionado")
        while True:
            while True:
                chute = input("Informe o número entre 0 e 1000: ")
                try:
                    chute = int(chute)
                    break
                except ValueError:
                    print("Informe um número inteiro")
            if 0 <= chute <= 1000:
                if chute == numero_certo:
                    print("Parabéns, vc acertou o número!")
                    break
                elif chute < numero_certo:
                    print("Errado, o número certo é MAIOR")
                elif chute > numero_certo:
                    print("Errado, o número certo é MENOR")
                else:
                    print("Valor Inválido!")
    if int(nivel) == 3:
        numero_certo = randint(-1, 1000001)
        print("Nível DIFÍCIL selecionado")
        while True:
            while True:
                chute = input("Informe o número entre 0 e 1.000.000: ")
                try:
                    chute = int(chute)
                    break
                except ValueError:
                    print("Informe um número inteiro")
            if 0 <= chute <= 1000000:
                if chute == numero_certo:
                    print("Parabéns, vc acertou o número!")
                    break
                elif chute < numero_certo:
                    print("Errado, o número certo é MAIOR")
                elif chute > numero_certo:
                    print("Errado, o número certo é MENOR")
                else:
                    print("Valor Inválido!")