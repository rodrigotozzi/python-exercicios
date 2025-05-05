"""
Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

class Pessoa:

    def __init__(self, nome, nascimento, email):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email

    @property
    def informe_nome(self):
        return self.__nome

    @informe_nome.setter
    def informe_nome(self, novo_nome):
        self.__nome = novo_nome


pessoa1 = Pessoa("Rodrigo", "Dezembro", "r@gmail.com")
print(pessoa1.informe_nome)

pessoa1 = pessoa1.informe_nome()

