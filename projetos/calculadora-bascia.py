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

def checa_int(entrada):
    try:
        int(entrada)
    except ValueError:
        print("Entrada Inválida")

def checa_float(entrada):
    try:
        float(entrada)
    except ValueError:
        print("Entrada Inválida")

while True:
    n1 = input("Informe o primeiro número: ")
    checa_int(n1)
    checa_float(n1)
    n2 = input("Informe o segundo número: ")
    checa_int(n2)
    checa_float(n2)