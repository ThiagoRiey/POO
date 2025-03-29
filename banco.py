class banco:
  # Método construtor
  def __init__(self, banco, agencia, conta, cliente, cpf):
    self.banco = banco
    self.agencia = agencia
    self.conta = conta
    self.cliente = cliente
    self.cpf = cpf
    self.saldo = 0
    self.senha = None

  # Método de definição de senha
  def definir_senha(self, new_senha):
    if self.senha == None:
        self.senha = new_senha
        print('Sua senha foi definida!')

    elif self.senha != None:
        decisao = input("Você já possui uma senha definida! Gostaria de mudar mesmo assim ? : ").lower
          if decisao == "sim":
              self.senha = new_senha
    else:
        print("Escolha errada!")
  # Método de apresentação
  def __srt__(self):
    return f"""
Cliente {self.cliente} cadastrado com sucesso
Conta: {self.conta}
Agencia: {self.agencia}
Banco: {self.banco}
""" 
  # deposito
  def Deposito(self, valor):
    if isinstance(valor, (int, float)):
        self.saldo += valor
        print(f"Saldo atualizado com sucesso no valor de R${float(valor)}")

  # saque
  def Saque(self, destinatario, valor):
    if self.senha == senha and salf.saldo >= valor and isinstance(valor, (int, float)):
      self.saldo -= valor
      print(f"Saque realizado no valor de: R${float(valor)}")
    else:
      print("Valor ou senha incorreta, tente novamente")

  # Pix
  def Pix(self, destinatario, valor):
    if isinstance(valor, (int, float)) and self.saldo >= valor:
      self.saldo -= valor
      destinatario.saldo += valor
                      f"""
Pix realizado no valor de R${valor}
De: {self.cliente}
Para: {destinatario.cliente}
"""
            )
    # Extrato
    def Extrato(self):
        print(
            f"""
-----------------------------------
Conta? {self.conta}
Agencia: {self.agencia}
Saldo: {self.saldo}
Cliente: {self.cliente}
-----------------------------------
            """
        )
zecove = Banco('Inter', 1, 1006, 'Ze das Coves', "987654321")

ze = Banco(" Saqua Eng Software", 1 , 1, "Ze da Manga", "123456789")

ze.definir_senha('admin01')

ze.Deposito(5000)

ze.Saque("admin01", 2500)

ze.Extrato()

zecove.definir_senha(5556666)

ze.Pix(zecove, 2000)

ze.Saque("admin01", 1000)

zecove.Extrato()

print(ze)

print(zecove)
        
  
