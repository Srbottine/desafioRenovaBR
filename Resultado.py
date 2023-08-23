import pandas as pd

# Carregue os DataFrames de perfil do eleitorado e resultados das eleições (já filtrados)
perfil_eleitorado_df = pd.read_csv('contagem_votos_limpo_sem_nulo.csv', encoding='utf-8', delimiter=',')
resultados_df = pd.read_csv('contagem_votos_limpo.csv', encoding='utf-8', delimiter=',')

# Dividir o perfil do eleitorado em partes menores
chunk_size = 10000  # Tamanho do pedaço
perfil_chunks = [perfil_eleitorado_df[i:i+chunk_size] for i in range(0, perfil_eleitorado_df.shape[0], chunk_size)]

# Inicializar um DataFrame vazio para resultados combinados
resultado_com_perfil_df = pd.DataFrame()

# Realize um JOIN entre os DataFrames com base no código do município em partes menores
for perfil_chunk in perfil_chunks:
    resultado_com_perfil_df = pd.concat([resultado_com_perfil_df, resultados_df.merge(perfil_chunk, on='CD_MUNICIPIO')])


# Encontre a lista de todos os partidos únicos na tabela
partidos_unicos = resultado_com_perfil_df['SG_PARTIDO_x'].unique()

# Itere por cada partido para obter as informações desejadas
for partido in partidos_unicos:
    # Em qual município o partido foi mais votado?
    municipio_mais_votado = resultado_com_perfil_df[resultado_com_perfil_df['SG_PARTIDO_x'] == partido] \
        .sort_values(by='QT_VOTOS_y', ascending=False).iloc[0]['NM_MUNICIPIO_y']

    # Qual foi a quantidade máxima de votos que o partido recebeu?
    max_votos = resultado_com_perfil_df[resultado_com_perfil_df['SG_PARTIDO_x'] == partido]['QT_VOTOS_y'].max()

    # Qual perfil do eleitorado mais votou nesse partido?
    perfil_eleitorado_mais_votou = resultado_com_perfil_df[
        (resultado_com_perfil_df['SG_PARTIDO_x'] == partido) &
        (resultado_com_perfil_df['QT_VOTOS_y'] == max_votos)
    ]
    
    print(f'Partido: {partido}')
    print(f'Município mais votado: {municipio_mais_votado}')
    print(f'Quantidade máxima de votos: {max_votos}')
  
    
    print('-' * 50)

