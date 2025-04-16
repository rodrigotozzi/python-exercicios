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

    def adicionar_contato(self):
        self.contato.append(input("Informe o nome do contato: "))

    def remover_contato(self):
        deletar = input("Informe o contato que gostaria de deletar: ")
        for i in self.contato:
            if i == deletar:
                self.contato.pop(deletar)

    def imprimir_agenda(self):
        print("Esses são os contatos da agenda:")
        for i in self.contato:
            print(i)

agenda1 = Agenda()

agenda1.adicionar_contato()
agenda1.adicionar_contato()
agenda1.imprimir_agenda()

agenda1.remover_contato()
agenda1.imprimir_agenda()