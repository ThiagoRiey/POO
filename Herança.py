class pessoa:
    def __init__(self, nome, sobrenome, altura, peso): #__init__  metodo para iniciar classe
        self.nome = nome
        self.sobrenome = sobrenome
        self.altura = altura
        self.peso = peso
        self.andar = False

    def __str__(self):  # __str__ Metodo para apresentar
        return f"""{self.nome} {self.sobrenome},{self.altura} Metros de altura, pesa {self.peso}Kg. """

    def Comecar_andar(self):
        if not self.andar:
            self.andar = True
        else:
            print('Você começou a andar')

    def parar(self):
        if self.andar:
            self.andar = False
            print("Você parou de andar")
        else:
            print("Você já está parado")
    
class Estudante(pessoa):
    def __init__(self, nome, sobrenome, altura, peso, curso):
        super().__init__(nome, sobrenome, altura, peso)    #Super - serve para herdar
        self.curso = curso
        self.conquistar = None
    
    def formar(self, diploma):
        if self.conquistar == None:
            if self.curso == diploma.nome_curso:
                self.conquistar = diploma
                print(f'O aluno {self.nome} conquistou o diploma de {self.conquistar.nome_curso}')
            else:
                print(f'Nome do curso não é o curso que o aluno {self.nome} faz')
                var = str(input(f'O aluno {self.nome} mudou de curso ? '))
                if var == 'sim' or var == "SIM" :
                    self.curso = diploma.nome_curso
                    self.conquistar = diploma
                    print(f'O aluno {self.nome} conquistou o diploma de {self.conquistar.nome_curso}')
                else:
                    print(f'O aluno {self.nome} não pode se forma nesse curso, pois ele está matriculado no curso de não
                          {self.curso}')
        else:
            print(f'O aluno {self.nome} já conquistou o seu diploma  de {self.conquistar.curso}')


class Diploma:
    def __init__(self, nome_curso):
        self.nome_curso = nome_curso

diploma = Diploma('Egenharia de Software')

ze = Estudante('ze', 'da manga', 1.65, 75, 'Nutrição')      

print(ze)  

ze.Comecar_andar()

print(f'O {ze.nome} {ze.sobrenome} chegou na facudade')

ze.parar()

print(f'O aluno `{ze.nome} {ze.sobrenome} terminou o curso e vai receber o diploma ')

ze.formar(diploma)
