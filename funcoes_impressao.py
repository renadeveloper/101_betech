from funcoes_calculo import obter_estatisticas

def imprimir_menu():
  print('\n--------------------------------------------------')
  print('\nEstatísticas do Brasileirão Série A de 2003 a 2019')
  print('\n--------------------------------------------------')
  print("\n------------------ MENU --------------------------\n")
  print("1. Exibir estatísticas de um time e ano específico")
  print("2. Exibir estatísticas de um time para cada ano de 2003 a 2019")
  print("3. Sair\n")

def imprimir_estatisticas(time,ano='todos'):
  time,vitorias, derrotas, empates, gols_mandante, gols_visitante, gols_contra_mandante, gols_contra_visitante = obter_estatisticas(time,ano)
  print('\n--------------------------------------------------')
  print('\nEstatísticas do Brasileirão Série A de 2003 a 2019')
  print('\n--------------------------------------------------')

  if ano == 'todos':
    print(f'\nAs estatísticas do time {time.title()} de 2003 a 2019 são:\n')
  else:
    print(f'\nAs estatísticas do time {time.title()} em {ano} são:\n')
  print('--------------------------------------------------')
  print(f'Partidas: {vitorias+derrotas+empates}')
  print(f'Vitórias: {vitorias}')
  print(f'Derrotas: {derrotas}')
  print(f'Empates: {empates}')
  print('--------------------------------------------------')
  print(f'Gols Pro: {gols_mandante+gols_visitante}')
  print(f'Gols Contra: {gols_contra_mandante+gols_contra_visitante}')
  print(f'Gols como Mandante: {gols_mandante}')
  print(f'Gols como Visitante: {gols_visitante}')
  print(f'Saldo de Gols: {(gols_mandante+gols_visitante)-(gols_contra_mandante+gols_contra_visitante)}')
