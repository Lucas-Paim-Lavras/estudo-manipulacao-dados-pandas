import pandas as pd
#carregando o dataset corretamente ==> neste caso, usa o separador ';'
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep = ';')    #É uma função do Pandas que puxa um arquivo CSV no computador

print(data)

#mostra as primeiras 5 linhas
print(data.head())  

#mostra as priemiras 10 lnhas
print(data.head(10))