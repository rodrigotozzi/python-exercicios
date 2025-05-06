"""
O computador escolhe um número e o usuário tenta adivinhar.
O jogo fornece dicas "maior" ou "menor"
"""

from random import randint

def checa_numero(entrada):
    try:
        return int(entrada)
    except ValueError:
        print("Valor Incorreto")

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
            chute = input("Informe o número entre 0 e 100: ")
            try:
                chute = int(chute)
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