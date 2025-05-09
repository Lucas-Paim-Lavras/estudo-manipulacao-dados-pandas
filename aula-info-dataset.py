import pandas as pd
#carregando o dataset corretamente ==> neste caso, usa o separador ';'
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep = ';')

print(data.info())  #fornece informações da quantidade de linhas, colunas

#Quando mandei o programa data.info() aparece que "PREÇO MÉDIO DISTRIBUIÇÃO", possui tipo de dado object ao invés de float. Esse object, no geral, representa strings. Isso parece estranho e suspeito. Veremos se isso é problemático mais pra frente.