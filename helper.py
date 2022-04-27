import os

menu = [[1,'X-Salada', 10.00],[2,'X-Burguer', 10.00],
[3,'Cachorro quente', 7.50],[4,'Misto quente', 8.00],
[5,'Salada de frutas', 5.50],[6,'Refrigerante', 4.50],
[7,'Suco natural', 6.25]]

def printSeparator(n):
  print('/' * n)

def verificarDados():
  cpf = input('Digite seu CPF: ')
  senha = input('Digite sua senha: ')
  try:
    with open(f'{cpf}.txt', 'r') as f:
      senhaCadastrada = f.readline().rstrip().split(':')[-1]
  except:
    print('NENHUM PEDIDO ENCONTRADO NO CPF INFORMADO!')

  return cpf, senha == senhaCadastrada
def cadastrarDados():
  dados = []
  printSeparator(50)
  dados.append(input('Digite seu nome: '))
  dados.append(input('Digite seu CPF: '))
  dados.append(input('Digite sua senha: '))
  with open(f'{dados[1]}.txt', 'w') as f:
    f.write(f"{dados[0]}:{dados[1]}:{dados[2]} \n\n")
  return dados[1]

def mostrarMenu():
    printSeparator(50)
    print("""
    CÓDIGO | PRODUTO          | PREÇO
    1      | X-Salada         | R$ 10,00
    2      | X-Burguer        | R$ 10,00
    3      | Cachorro quente  | R$ 7,50
    4      | Misto quente     | R$ 8,00
    5      | Salada de frutas | R$ 5,50
    6      | Refrigerante     | R$ 4,50
    7      | Suco natural     | R$ 6,25
    """)

def guardarPedidos(cpf, codigo, quantidade, opp = '+'):
    with open(f'{cpf}.txt', 'a') as f:
      f.write(f"{codigo}:{menu[codigo - 1][1]}:{menu[codigo - 1][2]}:{quantidade}:{opp}\n")

def adcionarProduto(cpf):
  mostrarMenu()
  codigo = int(input('Digite o codigo do produto: '))
  quantidade = int(input('Digite a quantidade deste produto: '))
  guardarPedidos(cpf, codigo, quantidade)

def removerProduto(cpf, codigo, quantidade):
  with open(f'{cpf}.txt') as f:
    f.readline()
    f.readline()
    adcionados = 0
    removidos = 0
    for linha in f:
     if (linha.split(':')[0] == codigo and linha.rstrip().split(':')[-1] == '+'):
       adcionados += int(linha.split(':')[-2]) 
     if (linha.split(':')[0] == codigo and linha.rstrip().split(':')[-1] == '-'):
       removidos += int(linha.split(':')[-2]) 
    if adcionados - removidos < int(quantidade):
      print('Não existe produtos o suficiente a ser removido!')
    else:
      guardarPedidos(cpf, int(codigo), int(quantidade), '-')
def calcularValor(cpf):
  with open(f'{cpf}.txt', 'r') as f:
    f.readline()
    total = 0
    for linha in f:
      if (linha.rstrip().split(':')[-1] == '+'):
       total += float(linha.split(':')[2]) * int(linha.split(':')[-2])
      elif (linha.rstrip().split(':')[-1] == '-'):
       total -= float(linha.split(':')[2]) * int(linha.split(':')[-2])
    return total