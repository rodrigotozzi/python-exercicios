"""
Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca;
"""

class Televisao:

    def __init__(self):
        self.status = False
        self.volume: int = 0
        self.canal: int = 0

    def estado_atual(self):
        print(f'A Televisão está {self.status}, no volume {self.volume} e canal {self.canal}')

    def liga_desliga(self):
        if self.status:
            self.status = False
        else:
            self.status = True
        print(f'A Televisão está {self.status}')

    def aumentar_volume(self):
        if self.volume == 10:
            print("Volume no nível máximo")
        elif 0 <= self.volume < 9:
            self.volume += 1
            print("Aumentou 1 unidade de volume")
        print(f'Volume Atual {self.volume}')

    def diminuir_volume(self):
        if self.volume == 0:
            print("Volume no nível mínimo")
        elif 0 < self.volume <= 10:
            self.volume -= 1
            print("Diminui 1 unidade de volume")
        print(f'Volume Atual {self.volume}')

    def aumentar_canal(self):
        if self.canal == 100:
            self.canal = 0
        elif 0 <= self.canal < 100:
            self.canal += 1
            print("Subiu 1 unidade do canal")
        print(f'Canal Atual {self.canal}')

    def diminuir_canal(self):
        if self.canal == 0:
            self.canal = 100
        elif 0 < self.canal <= 100:
            self.canal -= 1
            print("Diminuiu 1 unidade do canal")
        print(f'Canal Atual {self.canal}')

    def escolher_canal(self):
        while True:
            canal = int(input("Informe o canal que deseja sintonizar entre 0 e 100: "))
            if 0 <= canal < 100:
                self.canal = canal
                break
            else:
                print("Canal Inválido")
        print(f'Canal Atual {self.canal}')

class ControleRemoto:

    def __init__(self, tv):
        self.tv = tv

    def tv_conectada(self):
        print(f'A Televisão conectada é {self.tv}')

    def controle_liga_desliga(self):
        self.tv.liga_desliga()

tv1 = Televisao()
tv1.estado_atual()

controle1 = ControleRemoto(tv1)

tv1.liga_desliga()
tv1.liga_desliga()


"""
TESTE ESCOLHER CANAL
tv1.escolher_canal()

TESTE DIMINUIR CANAL
tv1.diminuir_canal()

TESTE AUMENTAR CANAL
tv1.aumentar_canal()

TESTE DIMINUIR VOLUME
tv1.diminuir_volume()

TESTE AUMENTAR VOLUME
tv1.aumentar_volume()

TESTE LIGA / DESLIGA
tv1.liga_desliga()
tv1.estado_atual()
"""

