"""
Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

class Agenda:

    def __init__(self):
        self.contato = []

    #Armazenar Contato
    def adicionar_contato(self):
        self.contato.append(input("Informe o nome do contato: "))

    #Remover Contato
    def remover_contato(self):
        deletar = input("Informe o contato que gostaria de deletar: ")
        if deletar in self.contato:
            self.contato.remove(deletar)
        else:
            print(f'Contato "{deletar}" não encontrado')

    #Informa em que posição da agenda está o contato
    def buscar_contato(self):
        buscar = input("Informe o nome do contato que deseja saber o indice: ")

        if buscar not in self.contato:
            print("Contato não localizado")
        else:
            print(f'O contato "{buscar}" está no indice "{self.contato.index(buscar)}"')

    #Imprimir Agenda
    def imprimir_agenda(self):
        print("Esses são os contatos da agenda:")
        for i in self.contato:
            print(i)

    #Imprime os dados do contato informado pelo índice
    def imprimir_contato(self):
        indice= int(input("Informe o indice do contato que deseja localizar: "))
        if indice > len(self.contato)-1:
            print(f'A lista só vai até o índice {len(self.contato)-1}')
        else:
            print(self.contato)

agenda1 = Agenda()

agenda1.adicionar_contato()
agenda1.adicionar_contato()
agenda1.imprimir_agenda()

agenda1.imprimir_contato()

"""
#TESTE BUSCAR
agenda1.buscar_contato()

#TESTE REMOVER
agenda1.remover_contato()
agenda1.imprimir_agenda()
"""