#Crie uma lista de tarefa, deve adicionar, remover e visualizar tarefa

def menu():
        while True:
            entrada = input("Adicionar tarefa: 1\nRemover tarefa: 2\nVisualizar tarefa:3\n")
            try:
                escolha = int(entrada)
                if escolha == 1:
                    return 1
                elif escolha == 2:
                    return 2
                elif escolha == 3:
                    return 3
                else:
                    print("Opção Inválida, insira um número de 1 a 3")
            except ValueError:
                return print("Entrada inválida, insira um número de 1 a 3")

def visualizar_lista():
    for i in lista_tarefa:
        


lista_tarefa = []

while True:
    print("**Lista de Tarefas**\nO que deseja fazer?")
    if menu() == 1:
        lista_tarefa.append(input("Qual tarefa gostaria de adicionar?\n"))
        print(lista_tarefa)
    elif menu() == 2:
        remover = input("")

