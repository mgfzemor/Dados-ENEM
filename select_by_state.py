'''
Programa para extrair apenas as variaveis que serao utilizadas na analize de dados
que deve receber os dados brutos do tipo: MICRODADOS_ENEM_20XX.csv e gera um novo arquivo data.bin
com os informacoes em binario.
'''
# DEFINITIONS =================================================================================
import struct, ast
# conta o numero de candidatos
i =0
# Definindo o type of struct
s = struct.Struct('l h 25s 2s h c h h h h h f f f f h c')
# END DEFINITIONS =================================================================================

'''
Dicionario de types:

fomart | C Type | size |
l      | long   |  4   |
h      | sort   |  2   |
c      | char   |  1   |
s      | char[] |  n   |
f      | float  |  4   |

Struct type utilizada:
('l h 25s 2s h c h h h h h f f f f h c')

Exemplo de dados:
candidato = (000000000001,2016,'PORTO ALEGRE','RS',18,'M',1,2013,1,1,1,636.90,670.20,676.10,678.30,760,'E')
'''


file_in = open('data/2014/dados.csv','r') # Arquivo com apenas alguns canditos para teste (base toda ocuparia muito espaco e levaria um certo tempo para upload)
line = file_in.readline() # Remove o cabecalho
while True:

    line = file_in.readline()
    v = line.split(',')
    i = i+1

    file_out = open('data/2014/estados/'+v[5]+'.bin','ab')
    # Cria uma 17upla com os dados corretos
    values = (v[0],v[1],v[3],v[5],v[15],v[16],v[22],v[23],v[24],v[25],v[27],v[70],v[71],v[72],v[73],v[89],v[92])
    # Converte em binario
    bin_values = s.pack(*values)
    # Escreve no novo arquivo apenas as variaveis uteis
    file_out.write(bin_values)
    file_out.close()
    if i%1000000 == 0:
        print 'ok'
