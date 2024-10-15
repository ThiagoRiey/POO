class Banco:
  def __init__(self, nome, saldo=0):
    self.nome = nome
    self.saldo = saldo
    self.senha = none

  def cadastrar_senha(self):
    if not self.senha:
      self.senha = input("Cadastrar sua senha: ")
      print("Senha cadastrada com sucesso!")
    else:
      print("Senha já cadastrada.")

  def verificar_senha(self):
    tentativa = input("Digite sua senha: ")
    return tentativa == self.senha

  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print(f'Depósito de R${valor} realizado com sucesso"')
    else:
      print("Valor de depósito inválido.")

  def consultar_saldo(self):
    print(f'Saldo atual: R${self.saldo}')

  def apresentar(self):
    print(f"Cliente: {self.nome}, Saldo: R${self.saldo}")

  def transferir(self, destinatario, valor):
    if self.saldo >= valor and valor > 0:
       if self.verificar_senha():
        self.saldo -= valor
        destinatario.saldo += valor
        print(f'Tranferência de R${valor} realizada para {destinatario.nome}.')
       else:
        print('Senha incorreta. transferência cancelada.')
    else:
      print("Transeferência inválida. Saldo insuficiente ou valor incorreto.")

@classmethod
def criar_conta(cls):
  nome = input("Digite o seu nome: ")
  cliente = cls(nome)
  cliente.cadastrar_senha()
  return cliente

@classmethod
def selecionar_conta(cls, clientes):
  if len(clientes) == 0:
     print("Nenhuma conta disponível. Crie uma conta primeiro.")
     return None

  print('=== Selecionar Conta ===')
  for idx, cliente in enumerate(clientes):
     print(f"{idx + 1}. {cliente.nome}")

  opcao = int(input("Escolha o número da conta: "))
  if 1 <= opcao <= len(clientes):
    return clientes[opcao - 1]
  else:
      print("Opção inválida.")
      return None

      while True:
         print('=== menu do Banco ===')
         print('1. Criar Conta')
         print('2. Selecionar Conta')
         print('3. Depositar')
         print('4. Consultar saldo')
         print('5. Apresentar dados')
         print('6. transferir')
         print('7. Sair')

         opcao = input("Escolha uma opção: ")
         if opcao == '1':
            novo_cliente = cls.criar_conta()
            cliente.append(novo_cliente)
         elif opcao == "2":
            cliente_selecionado = cls.selecionar_conta(clientes)
         elif opcao == '3':
            if cliente_selecionado:
              valor = float(input("Informe o valor para depósito: "))
              cliente_selecionado.depositar(valor)
            else:
              print("Você precisa selecionar uma conta prinmeiro!")
