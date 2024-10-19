class pessoa:
    def __init__(self, nome):
        self.Nome = nome
        self.chavest = False

    def abrir(self, porta):
        if porta.EstaAberta == False and porta.EstaTrancada == False:
            porta.EstaAberta == True
            print(f"{self.Nome} abriu a porta!")

        elif porta.EstaTrancada == True:
            print('Destranque a porta para abrir.')

        else:
            print('A porta já esta aberta!')

    def fechar(self, porta):
        if porta.EstaAberta:
            porta.EstaAberta = False
            print(f'{self.Nome} fechou a porta!')
        else:
            print('A porta ja esta fechada!')

    def pegarchave(self, chave):
        if not self.chavest:
            self.chavest = True
            print(f'{self.Nome} pegou a chave.')

    def Inserir(self, chave, porta):
        if self.chavest:
            if porta.Macaneta.Chave == None:
                porta.Macaneta.Chave = chave
                print(f'{self.Nome} iseriu a chave na porta')

class Porta:
    def __init__(self, macaneta):
        self.Macaneta = macaneta
        self.EstaAberta = False
        self.EstaTrancada = True

class Macaneta:
    def __init__(self):
        self.EstaVirada = False
        self.Chave = None

    def RodarChave(self, pessoa, porta):
        if self.Chave != None:
            if not self.Chave.EstaVirada:
                self.Chave.EstaVirada = True
                porta.EstaTrancada = False
                print(f'{pessoa.Nome} girou a chave!')
            else:
                porta.EstaTrancada = True
                print("Você girou a chave e trancou a porta")
        else:
            print('Ponha a chave na maçaneta.')

class Chave:
    def __init__(self, marca):
        self.Marca = marca
        self.EstaVirada = False

pessoa1 = pessoa('Riey')
macaneta = Macaneta()
porta1 = Porta(macaneta)
chaves = Chave('Platina')

print('1 - Tentando abrir a porta sem a chave: ')
pessoa1.abrir(porta1)

print('\n2 - Tentando destrancar sem a chave: ')
macaneta.RodarChave(pessoa1, porta1)

print('\n3 - Pegando a chave: ')
pessoa1.pegarchave(chaves)

print('\n4 - Inserindo a chave na maçaneta')
pessoa1.Inserir(chaves, porta1)

print('\n5 - Rodando a chave para destrancar a porta.')
macaneta.RodarChave(pessoa1, porta1)

print('\n6 - Pessoa abrindo a porta após ter pego a chave, inserido na porta e rodar')
pessoa1.abrir(porta1)

print('7 - Fechando a porta')
        
