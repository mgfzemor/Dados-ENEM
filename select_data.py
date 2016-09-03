'''
Programa para extrair apenas as variaveis que serao utilizadas na analize de dados
que deve receber os dados brutos do tipo: MICRODADOS_ENEM_20XX.csv e gera um novo arquivo data_out.csv
'''
from classes.student import Student
file_in = open('data_in.csv','r') # Arquivo com apenas alguns canditos para teste (base toda ocuparia muito espaco e levaria um certo tempo para upload)
file_out = open('data_out.csv','w')
data = file_in.readlines()
for line in data:
    # separa todos os dados em uma List
    v = line.split(',')
    # Escreve no novo arquivo apenas as variaveis uteis
    file_out.write(v[0]+';'+v[1]+';'+v[3]+';'+v[5]+';'+v[15]+';'+v[16]+';'+v[22]+';'+v[23]+';'+v[24]+';'+v[25]+';'+v[27]+';'+v[70]+';'+v[71]+';'+v[72]+';'+v[73]+';'+v[89]+';'+v[92]+'\n')
