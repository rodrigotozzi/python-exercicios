# Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
# setters para os atributos e um metodo para imprimir os dados de uma pessoa.

class Pessoa:

    def __init__(self):
        self.nome = input("Informe o nome: ")
        self.nascimento = input("Informe a data de nascimento: ")
        self.email = input("Informe o e-mail: ")

    def definir_nome(self):
        self.nome = input("Informe o nome: ")

    def definir_email(self):
        self.email = input("Infome o e-mail: ")

    def definir_nascimento(self):
        self.nascimento = input("Informe a data de nascimento: ")

    def mostrar_dados(self):
        print(f'{self.nome} nasceu em {self.nascimento} e tem o e-mail {self.email}')

pessoa1 = Pessoa()
pessoa1.mostrar_dados()

pessoa1.definir_nome()
pessoa1.definir_nascimento()
pessoa1.definir_email()
pessoa1.mostrar_dados()
