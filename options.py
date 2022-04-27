import helper as h
import os

def criarPedido():
  cpf = h.cadastrarDados()
  while True:
    h.adcionarProduto(cpf) 
    inp = input('Deseja adcionar outro produto (sim / não): ')
    if inp == 'não':
      break
def cancelarPedido():
  cpf, autorizado = h.verificarDados()
  if autorizado:
    os.remove(f'{cpf}.txt')
def inserirProduto():
  cpf, autorizado = h.verificarDados()
  if autorizado:
    h.adcionarProduto(cpf)
def excluirProduto():
  cpf, autorizado =  h.verificarDados()
  h.mostrarMenu()
  codigo = input('Digite o codigo do produto a ser removido: ')
  quantidade = input('Digite a quantidade do produto a ser removido: ')
  if autorizado:
    h.removerProduto(cpf, codigo, quantidade)
def exibirTotal():
  cpf, autorizado = h.verificarDados()
  if autorizado:
    total = h.calcularValor(cpf)
    print(f'Total a ser pago: R${total:.2f}')

def exibirExtrato():
  cpf, autorizado = h.verificarDados()
  if autorizado:
    with open(f'{cpf}.txt', 'r') as f:
      f.readline()
      f.readline()

      print('CODIGO | NOME          | VALOR | QUANTIDADE | OPP')
      for line in f:
        codigo, nome, valor, quantidade, opp = line.rstrip().split(':')
        print(f'{codigo:<6} | {nome:<13} | {valor:<3}  | {quantidade:<6}     | {opp:<2}')

