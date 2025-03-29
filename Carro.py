# definindo o método construtor da classe
class Carro:
    def __init__(self, marca, modelo, ano, cor, placa, marcha):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        self.marcha = 0
    

    # Método de classe
    def __str__(self):
        return f"""
O carro de Marca {self.marca} e modelo {self.modelo}
do ano {self.ano} e cor {self.cor} saiu da loja e hoje tem a placa
{self.placa}
            """
    
    # método de instância
    @classmethod
    def cadastro_venda(cls):
        marca = input("Digite aqui a marca do carro comprado: ")
        modelo = input("Digite aqui o modelo do carro comprado: ")
        ano = int(input("Digite aqui o ano do carro comprado: "))
        cor = input("Digite aqui a cor do carro comprado: ")
        placa = input("Digite aqui a placa do carro comprado: ")
        return cls(marca, modelo, ano, cor, placa)
    
    
    def ligar_carro(self):
        if not self.is_running and self.marcha == 0:
            self.marcha = 0 
            self.is_running = True
            print("O carro foi ligado..... RUMRUMRUMRUM")
        else:
            print("O carro já esta ligado!!!")
    
    def acelerar(self):
        if self.is_running and self.marcha == 0:
            self.marcha = 1 
            self.velocidade += 30
            print(f"A velocidade do carro é {self.velocidade}km/h")
        elif self.is_running and self.marcha == 1 and self.velocidade <= 20:
            self.marcha = 2
            self.velocidade += 35
            print(f"A velocidade do carro é {self.velocidade}km/h")
        elif self.is_running and self.marcha == 2 and self.velocidade <= 40:
            self.marcha = 3
            self.velocidade += 40
            print(f"A velocidade do carro é {self.velocidade}km/h")
        else:
            print(f"O carro {self.modelo} esta desligado precisa ligar o carro primeiro!!!")

    def freiar(self):
        if self.is_running and self.velocidade > 0:
            self.velocidade -= 5
            print(f"A velocidade do carro é {self.velocidade}km/h")
        else:
            print(f"O carro {self.modelo} esta desligado ou sua velocidade já é 0 km/h precisa ligar o carro primeiro!!!")
    # e o carro precisa ser desligado
    def desligar(self):
        if self.is_running:
            self.is_running = False
            print(f'{self.modelo} foi desligado!')
        else:
            print(f'o {self.modelo} já esta desligado')

# montar um acelerador que ira acelerar com base na marchar definida
    def marchar(self):
        if self.is_running < 20:
            return 1
        elif self.is_running < 40:
            return 2
        elif self.is_running < 60:
            return 3
        elif self.is_running < 80:
            return 4
        else:
            return 5
# para o carro da a ré ele precisa esta entre 1 km/h ou parado
    def re(self):
        if self.is_running == 0 < 1:
            print(f'o carro{self.modelo} começou a dar ré')
        else:
            return

# Método de apresentação

Thi = Carro('Peugeot',206, 2009,'vermelho', 'RIO96')
print(Thi)
