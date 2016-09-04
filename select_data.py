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


file_in = open('MICRODADOS_ENEM_2014.csv','r') # Arquivo com apenas alguns canditos para teste (base toda ocuparia muito espaco e levaria um certo tempo para upload)
file_out = open('data/data.bin','wb')
line = file_in.readline() # Remove o cabecalho
while True:
    line = file_in.readline()
    v = line.split(',')
    i = i+1
    # CASTING variables ================================================================================
    # Verica se existe um numero de inscricao eh nulo, caso positivo chegou o final do arquivo
    if v[0]== '':
        break
    else:
        v[0] = ast.literal_eval(v[0])
    v[1] = ast.literal_eval(v[1])

    # Validacao de dados
    if v[5] == '':   # UF
        v[16] = 'NI' #  NI = nao informada
    if v[15] == '':  # idade
        v[15] = 0
    else:
        v[15] = ast.literal_eval(v[15])
    if v[16] == '':  # Sexo
        v[16] = 'O'  # Outro
    if v[22] == '':  # Situacao conclusao
        v[22] = 0    # 0 = nao informado
    else:
        v[22] = ast.literal_eval(v[22])
    if v[23] == '':  # Ano Cloncluiu
        v[23] = 0
    else:
        v[23] = ast.literal_eval(v[23])
    if v[24] == '':  # Tipo Escola
        v[24] = 0
    else:
        v[24] = ast.literal_eval(v[24])
    if v[25] == '':  # in_tp_ensino
        v[25] = 0
    else:
        v[25] = ast.literal_eval(v[25])
    v[27] = ast.literal_eval(v[27])
    # Verifica se alguma nota esta vazia, caso positivo coloca zero como nota
    if v[70] == '':
        v[70] = 0
    else:
        v[70] = ast.literal_eval(v[70])
    if v[71] == '':
        v[71] = 0
    else:
        v[71] = ast.literal_eval(v[71])
    if v[72] == '':
        v[72] = 0
    else:
        v[72] = ast.literal_eval(v[72])
    if v[73] == '':
        v[73] = 0
    else:
        v[73] = ast.literal_eval(v[73])
    if v[89] == '':
        v[89] = 0
    else:
        v[89] = ast.literal_eval(v[89])
    if v[92] == '':
        v[92] = 'Z' # Z = nao informado
    # END CASTING ===================================================================================

    # Cria uma 17upla com os dados corretos
    values = (v[0],v[1],v[3],v[5],v[15],v[16],v[22],v[23],v[24],v[25],v[27],v[70],v[71],v[72],v[73],v[89],v[92])
    # Converte em binario
    bin_values = s.pack(*values)
    # Escreve no novo arquivo apenas as variaveis uteis
    file_out.write(bin_values)
