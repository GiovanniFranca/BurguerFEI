import helper as h
import options as op

while True:
  h.printSeparator(50)
  print("""
  1. - Novo Pedido
  2. - Cancelar Pedido
  3. - Insere produto
  4. - Remove produto
  5. - Valor do pedido
  6. - Extrato do pedido


  0 - Sair
  """)
  option = input("Selecione uma opção: ")
  try:
    option = int(option)
  except:
    print('Valor inválido!')
    continue
  if option == 0:
    quit()

  if (option < 0 or option > 6):
    print("\nSELECIONE UM NÚMERO ENTRE 1 E 6")

  if option == 1:
    op.criarPedido()
  if option == 2:
    op.cancelarPedido()
  if option == 3: 
    op.inserirProduto()
  if option == 4:
    op.excluirProduto()
  if option == 5:
    op.exibirTotal()
  if option == 6:
    op.exibirExtrato()