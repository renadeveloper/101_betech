from funcoes_input import solicitar_ano,solicitar_time
from funcoes_impressao import imprimir_estatisticas, imprimir_menu

def main_loop ():
  while True:
    imprimir_menu()

    try:
      time = None
      ano = None
      opcao = int(input("Escolha uma opção: "))
      if opcao == 1:
        time = solicitar_time()

        if (time is not None):
          ano = solicitar_ano()

        if (ano is not None):
          imprimir_estatisticas(time,ano)

      elif opcao == 2:
        time = solicitar_time()

        if (time is not None):
          imprimir_estatisticas(time)

      elif opcao == 3:
        print("\nSaindo do programa...")
        break
      else:
        print("\nOpção inválida. Tente novamente.")

    except ValueError:
      print("\nEntrada inválida. Por favor, digite uma opção de menu válida.")
