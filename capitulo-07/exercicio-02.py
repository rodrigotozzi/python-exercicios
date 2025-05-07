"""
Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
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

class Carro(Veiculo):
    def __init__(self, marca, modelo, porta):
        super().__init__(marca, modelo)
        self._porta = porta

    @property
    def dados_veiculo(self):
        return f'Marca: {self._marca} Modelo: {self._modelo} Quantidade de Portas: {self._porta}'
