"""
Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

class Pessoa:

    def __init__(self, nome, nascimento, email):
        self._nome = nome
        self._nascimento = nascimento
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_nascimento):
        self._nascimento = novo_nascimento

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def dados_pessoal(self):
        return f'Nome: {self._nome}\nData de Nascimento: {self._nascimento}\nEmail: {self._email}'


pessoa1 = Pessoa("Rodrigo", "Dezembro", "@gmail.com")
