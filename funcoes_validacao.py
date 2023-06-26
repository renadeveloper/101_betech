def validar_nome_time(nome_time):
  if any(caractere.isdigit() for caractere in nome_time):
    return False
  if any((caractere in 'áàâãéèêíïóôõöúüç') for caractere in nome_time):
    return False
  return True

def validar_ano(ano):
  if (len(ano) != 4 and (not ano.isdigit())):
    return False
  return True  