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

def receber_checar_entrada():
    while True:
        entrada = input("Informe o número: ")
        try:
            valor = float(entrada)
            if valor == int(valor):
                return int(entrada)
            else:
                return float(valor)
        except ValueError:
            print("Entrada Inválida, informe um número")

def escolher_operacao():
    while True:
        print("Qual operação deseja realizar?")
        escolha = input("Adição: 1\nSubtração: 2\nMultiplicação: 3\nDivisão: 4\n")
        try:
            valor = int(escolha)
            if valor == 1:
                return 1
            elif valor == 2:
                return 2
            elif valor == 3:
                return 3
            elif valor == 4:
                return 4
            else:
                print("Valor informado inválido, escolha uma operação de 1 a 4")
        except ValueError:
            print("Entrada Inválida, informe um valor de 1 a 4")

def repetir_operacao():
    while True:
        repetir = input("Gostaria de fazer outro cálculo?\nSim: 1\nNão: 2\n")
        try:
            repetir = int(repetir)
            if repetir == 1:
                return 1
            elif repetir == 2:
                return 2
            else:
                print("Valor inválido, digite 1 ou 2\n")
        except ValueError:
            print("Entrada Inválida, informe 1 ou 2\n")


while True:
    entrada1 = receber_checar_entrada()
    entrada2 = receber_checar_entrada()
    operacao = escolher_operacao()
    if operacao == 1:
        print(adicao(entrada1, entrada2))
        reiniciar = repetir_operacao()
        if reiniciar == 1:
            print("Calculadora reiniciada...")
        elif reiniciar == 2:
            print("Calculadora finalizada, até a próxima.")
            break
    elif operacao == 2:
        print(subtracao(entrada1, entrada2))
        reiniciar = repetir_operacao()
        if reiniciar == 1:
            print("Calculadora reiniciada...")
        elif reiniciar == 2:
            print("Calculadora finalizada, até a próxima.")
            break
    elif operacao == 3:
        print(multiplicacao(entrada1, entrada2))
        reiniciar = repetir_operacao()
        if reiniciar == 1:
            print("Calculadora reiniciada...")
        elif reiniciar == 2:
            print("Calculadora finalizada, até a próxima.")
            break
    elif operacao == 4:
        print(divisao(entrada1, entrada2))
        reiniciar = repetir_operacao()
        if reiniciar == 1:
            print("Calculadora reiniciada...")
        elif reiniciar == 2:
            print("Calculadora finalizada, até a próxima.")
            break
