"""
Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.
"""

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nova_marca):
        self._marca = nova_marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self._modelo = novo_modelo

    @property
    def dados_veiculo(self):
        return self._marca, self._modelo

veiculo1 = Veiculo("Ford", "Fiesta")
print(veiculo1.dados_veiculo)
