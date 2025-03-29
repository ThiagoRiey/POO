class Pessoa:
  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

pessoa = Pessoa('João', 26, 12345678912)

print(pessoa)
