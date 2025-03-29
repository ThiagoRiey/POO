class Pessoa:
  def __init__(self, nome, idade, cpf): #__init__  é o método construtor em python
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

pessoa = Pessoa('João', 26, 12345678912)

print(pessoa)
