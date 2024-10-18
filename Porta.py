class Chave:
    def _init_(self, codigo):
        self.codigo = codigo

class Macaneta:
    def _init_(self):
        self.girada = False

    def girar(self):
        self.girada = True
        print("A maçaneta foi girada.")

    def resetar(self):
        self.girada = False
        print("A maçaneta foi resetada.")

class porta:
    def _init_(self):
        self.aberta = False
        self.macaneta = Macaneta()

    def abrir(self, chave):
        if self.macaneta.girada:
            self.aberta = True
            print("A porta está aberta.")
        else:
            print("A maçaneta não foi girada. A porta não pode ser aberta.")

    def fechar(self):
        if self.aberta:
            self.aberta = False
            self.macaneta.resetar()
            print("A porta está fechada.")
        else:
            print("A porta já está fechada.")


