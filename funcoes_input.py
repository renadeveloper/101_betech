from funcoes_validacao import validar_nome_time, validar_ano

def solicitar_time():
  try:
    time = input("\nDigite o nome do time sem acentos: ").strip().lower()
    if (not validar_nome_time(time)):
      raise ValueError("Time inválido. Digite um time somente com letras.")

  # Exceções de validação do nome do time
  except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
  except ValueError as e:
    print(e)

  if validar_nome_time(time):
    return time
  else:
    return None

def solicitar_ano():
  try:
    ano = input("Digite o ano: ").strip()
    if (not validar_ano(ano)):
      raise ValueError("Ano inválido. Digite um ano com 4 dígitos.")

  # Exceções de validação do ano
  except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
  except ValueError as e:
    print(e)

  if validar_ano(ano):
    return ano
  else:
    return None