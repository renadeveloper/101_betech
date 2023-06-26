import csv

def obter_estatisticas(time, ano):
  with open('campeonato-brasileiro-full.csv', 'r', encoding='utf-8') as arquivo:
    vitorias, derrotas, empates = 0,0,0
    leitor_csv = csv.DictReader(arquivo)

    if (ano == 'todos'):
      vitorias = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() == time))

      volta_para_inicio_arquivo(arquivo)

      gols_mandante = sum(int(linha['mandante_Placar']) for linha in leitor_csv
                          if (linha['mandante'].lower() == time))

      volta_para_inicio_arquivo(arquivo)

      gols_visitante = sum(int(linha['visitante_Placar']) for linha in leitor_csv
                          if (linha['visitante'].lower() == time))

      volta_para_inicio_arquivo(arquivo)

      gols_contra_mandante = sum(int(linha['visitante_Placar']) for linha in leitor_csv
                          if (linha['mandante'].lower() == time))

      volta_para_inicio_arquivo(arquivo)

      gols_contra_visitante = sum(int(linha['mandante_Placar']) for linha in leitor_csv
                          if (linha['visitante'].lower() == time))

      volta_para_inicio_arquivo(arquivo)

      empates = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() == '-'))

      volta_para_inicio_arquivo(arquivo)

      derrotas = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() != time
                      and linha['vencedor'].lower() != '-'))
    else:
      vitorias = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() == time
                      and obter_ano_da_data(linha['data']) == ano))

      volta_para_inicio_arquivo(arquivo)

      gols_mandante = sum(int(linha['mandante_Placar']) for linha in leitor_csv
                          if (linha['mandante'].lower() == time)
                          and obter_ano_da_data(linha['data']) == ano)

      volta_para_inicio_arquivo(arquivo)

      gols_visitante = sum(int(linha['visitante_Placar']) for linha in leitor_csv
                          if (linha['visitante'].lower() == time)
                          and obter_ano_da_data(linha['data']) == ano)

      volta_para_inicio_arquivo(arquivo)

      gols_contra_mandante = sum(int(linha['visitante_Placar']) for linha in leitor_csv
                          if (linha['mandante'].lower() == time)
                          and obter_ano_da_data(linha['data']) == ano)

      volta_para_inicio_arquivo(arquivo)

      gols_contra_visitante = sum(int(linha['mandante_Placar']) for linha in leitor_csv
                          if (linha['visitante'].lower() == time)
                          and obter_ano_da_data(linha['data']) == ano)

      volta_para_inicio_arquivo(arquivo)

      empates = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() == '-'
                      and obter_ano_da_data(linha['data']) == ano))

      volta_para_inicio_arquivo(arquivo)

      derrotas = sum(1 for linha in leitor_csv
                      if ((linha['mandante'].lower() == time
                      or linha['visitante'].lower() == time)
                      and linha['vencedor'].lower() != time
                      and linha['vencedor'].lower() != '-'
                      and obter_ano_da_data(linha['data']) == ano))

  return time, vitorias, derrotas, empates, gols_mandante, gols_visitante, gols_contra_mandante, gols_contra_visitante

def obter_ano_da_data(data):
  dia, mes, ano = data.strip().split('/')
  return ano

def volta_para_inicio_arquivo(arquivo):
  arquivo.seek(0)
