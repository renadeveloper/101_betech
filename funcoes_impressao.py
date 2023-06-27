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
  try:
    time,vitorias, derrotas, empates, *gols = obter_estatisticas(time,ano)
    partidas = vitorias+empates+derrotas
    gols_mandante = gols[0]
    gols_visitante = gols[1]
    gols_contra_mandante = gols[2]
    gols_contra_visitante = gols[3]
    gols_pro = gols_mandante+gols_visitante
    gols_contra = gols_contra_mandante + gols_contra_visitante
    saldo_gols = gols_pro - gols_contra
    
    print('\n--------------------------------------------------')
    print('\nEstatísticas do Brasileirão Série A de 2003 a 2019')
    print('\n--------------------------------------------------')

    if ano == 'todos':
      print(f'\nAs estatísticas do time {time.title()} de 2003 a 2019 são:\n')
    else:
      print(f'\nAs estatísticas do time {time.title()} em {ano} são:\n')
      print(f'Partidas: {partidas}')
      print(f'Vitórias: {vitorias}')
      print(f'Derrotas: {derrotas}')
      print(f'Empates: {empates}')
      print('--------------------------------------------------')
      print(f'Gols Pro: {gols_pro}')
      print(f'Gols Contra: {gols_contra}')
      print(f'Gols como Mandante: {gols_mandante}')
      print(f'Gols como Visitante: {gols_visitante}')
      print(f'Saldo de Gols: {saldo_gols}')

      if partidas == 0:
        print('Não foram disputadas partidas.')

      media_gols_pro = gols_pro / partidas
      media_gols_contra = gols_contra / partidas
      print(f'Média de Gols Pro por partida: {round(media_gols_pro, 2)}')
      print(f'Média de Gols Contra por partida: {round(media_gols_contra, 2)}')
  except ZeroDivisionError:
    print('Erro: Não é possível calcular as médias sem partidas disputadas.')

  print('--------------------------------------------------')
