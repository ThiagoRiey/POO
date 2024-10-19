class Automovel:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print('O veículo já está ligado')

    def desligar(self):     
