#Implemente as operações básicas de uma calculadora (Adição, Subtração, Multiplicação e Divisão)

def adicao(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1,numero2):
    return numero1*numero2

def divisao(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        return "Não é possível dividir por 0"
    else:
        return numero1/numero2

def verificar_entrada(entrada):
    try:
        valor = float(entrada)
        if valor == int(valor):
            return int(valor)
        else:
            return float(valor)
    except ValueError:
        return "Entrada Inválida, informe um número"


while True:
    while True:
        n1 = input("Informe o primeiro número: ")
        try:
            valor = float(n1)
            if valor == int(valor):
                valor = int(valor)
                break
            else:
                valor = float(valor)
                break
        except ValueError:
            print("Entrada Inválida, informe um número")

"""    while True:
        n2 = input("Informe o segundo número: ")
        if verificar_entrada(n2) == int(n2) or verificar_entrada(n2) == float(n2):
            validacao2 = True
            break
        else:
            print(verificar_entrada(n2))"""
    #print("Qual operação deseja realizar?")
    #escolha = input("Adição: 1\nSubtração: 2\nMultiplicação: 3\nDivisão: 4\n")
