import tkinter as tk
from tkinter import messagebox


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # método que é abstrato 
    def apresentar(self):
        raise NotImplementedError("Subclasse deve implementar o método apresentado")

    # 1ª subclass e Herança   
class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        return f"Sou o aluno {self.nome} do  curso {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Sou professor {self.nome} do curso {self.disciplina}"
    
#função poliformica
def apresentar_pessoa(pessoa: Pessoa):
    return pessoa.apresentar()

#class cria a interface grafica
class SistemaApresentacoes:
    def __init__(self, pessoas):
        self.pessoas = pessoas 
    
        #criando a interface gráfica
        self.janela = tk.Tk()
        #criando o título
        self.janela.title("Sistema de Apresentações")
        #definindo o tamanho
        self.janela.geometry("300x150")

        #criando o botão
        self.botao = tk.Button(self.janela, text="Mostrar a apresentações", command=self.apresentar_pessoa)
        self.botao.pack(pady=40)

    #criando um método que absorve o método polifórmico 
    def apresentar_pessoa(self):

        mensagens = [apresentar_pessoa(p) for p in self.pessoas]

        messagebox.showinfo("Apresentações", "\n".join(mensagens))

    def iniciar(self):
        self.janela.mainloop()


aluno = Aluno("Riey", "Engenharia de Software")
professor = Professor("Diego", "POO")
pessoas = [aluno, professor]

sistema = SistemaApresentacoes(pessoas)
sistema.iniciar()
