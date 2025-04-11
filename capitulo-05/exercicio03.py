#Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.

def lista_maior_valor():
    maior_valor = 0
    lista = []
    while True:
        valor = input("Informe um valor para a lista ou digite SAIR: ")
        if valor.upper() == "SAIR":
            break
        else:
            lista.append(int(valor))

    for i in lista:
        if i > maior_valor:
            maior_valor = i
    return maior_valor

print(lista_maior_valor())
