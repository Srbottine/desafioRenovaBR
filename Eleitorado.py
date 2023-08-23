import pandas as pd

# Carregue o arquivo de perfil do eleitorado em um DataFrame
perfil_eleitorado_df = pd.read_csv('perfil_eleitorado_2020.csv', encoding='latin1', delimiter=';')


# Selecione apenas as colunas relevantes
colunas_perfil_eleitorado = [
    'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO', 'CD_GENERO', 'DS_GENERO',
    'CD_ESTADO_CIVIL', 'DS_ESTADO_CIVIL', 'CD_FAIXA_ETARIA', 'DS_FAIXA_ETARIA',
    'CD_GRAU_ESCOLARIDADE', 'DS_GRAU_ESCOLARIDADE', 'QT_ELEITORES_PERFIL'
]
perfil_eleitorado_df = perfil_eleitorado_df[colunas_perfil_eleitorado]

# Identifique registros em branco ou nulos e remova-os da base
perfil_eleitorado_df.dropna(inplace=True)

# Crie uma tabela limpa para o perfil do eleitorado
perfil_eleitorado_limpo_df = perfil_eleitorado_df.copy()

# Salve a tabela limpa em um novo arquivo CSV 
perfil_eleitorado_limpo_df.to_csv('perfil_eleitorado_limpo.csv', index=False, encoding='utf-8')

# Visualize as primeiras linhas da tabela limpa 
print("\nPerfil do Eleitorado Limpo:")
print(perfil_eleitorado_limpo_df.head())

resultados_df = pd.read_csv('SP_turno_1.csv', encoding='latin1', delimiter=';')



# Selecione apenas as colunas relevantes para os resultados das eleições
# Filtrar os dados onde 'SG_PARTIDO' não é igual a '#NULO#'
resultados_df = resultados_df[resultados_df['SG_PARTIDO'] != '#NULO#']

# Inclua as colunas 
colunas_resultados = ['CD_MUNICIPIO', 'NM_MUNICIPIO', 'NR_ZONA', 'SG_PARTIDO', 'NM_PARTIDO', 'QT_VOTOS']
resultados_df = resultados_df[colunas_resultados]

# Agrupe os dados por município, zona eleitoral, partido e some a quantidade de votos
votos_por_municipio_zona_partido = resultados_df.groupby(['CD_MUNICIPIO', 'NM_MUNICIPIO', 'NR_ZONA',  'SG_PARTIDO', 'NM_PARTIDO'])['QT_VOTOS'].sum().reset_index()

# Visualize as primeiras linhas da tabela com a contagem de votos
print("Contagem de Votos por Município, Zona Eleitoral e Partido:")
print(votos_por_municipio_zona_partido.head())

# Salve a tabela com a contagem de votos em um novo arquivo CSV 
votos_por_municipio_zona_partido.to_csv('contagem_votos_limpo_sem_nulo.csv', index=False, encoding='utf-8')


