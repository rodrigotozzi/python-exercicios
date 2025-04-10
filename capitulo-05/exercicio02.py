# Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
# imprima ela por extenso como “1 de janeiro de 20204”.

def data_extenso():
    data = input("Informe a data no modelo dd/mm/aaaa: ")
    data = data.split("/")
    dia = data[0]
    mes = data[1]
    if mes == "01":
        mes = "Janeiro"
    elif mes == "02":
        mes = "Fevereiro"
    elif mes == "03":
        mes = "Março"
    elif mes == "04":
        mes = "Abril"
    elif mes == "05":
        mes = "Maio"
    elif mes == "06":
        mes = "Junho"
    elif mes == "07":
        mes = "Julho"
    elif mes == "08":
        mes = "Agosto"
    elif mes == "09":
        mes = "Setembro"
    elif mes == "10":
        mes = "Outubro"
    elif mes == "11":
        mes = "Novembro"
    elif mes == "12":
        mes = "Dezembro"
    ano = data[2]
    print(f'{dia} de {mes} de {ano}')

data_extenso()
