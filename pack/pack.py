'''
Dicionario de types:

fomart | C Type | size |
l      | long   |  4   |
h      | sort   |  2   |
c      | char   |  1   |
s      | char[] |  n   |
f      | float  |  4   |
'''

import struct
from classes.student import *
# inscricao,ano,cod_municipio,municipio,cod_uf,uf,cod_escola,idade,sexo,tp_escola,raca,p_cn,p_ch,p_lc,p_mt,nota_cn,nota_ch,nota_lc,nota_mt,nota_redacao,renda
aluno_struct =  struct.Struct('l h l 25s h 2s l h c h h h h h h f f f f h c')
# id_esc,ano,codigo,nome,situacao,municipio,uf,tipo_escola,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos
escola_struct = struct.Struct('l h l 50s h l l h f f f f f f l')
# id_municipio,cod_municipio,municipio,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos,total_escolas
municipio_struct = struct.Struct('l l 50s f f f f f f l l')
#id_uf,cod_uf,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos,total_escolas,total_municipios
estado_struct = struct.Struct('l l f f f f f f l l l')

# ================ DB_MUNICIPIO ==================
# id,cod_municipio,qtd_alunos
lista_alunos_struct = struct.Struct('l l l')
#id,cod_municipio,qtd_escolas
lista_escolas_struct = struct.Struct('l l l')
# inteiro
int_struct = struct.Struct('l l')
#
index_municipio_struct = struct.Struct('l l l l')
# ============== END DB_MUNICIPIO =================

'''
Funcao que recebe um tipo de estrutura e um arquivo, e retorna
uma lista de tuplas
'''
def unpack_data(type_struct,file_name):
    file_data = open(file_name,'rb')
    lista = []
    i=0
    while True:
        data = file_data.read(type_struct.size)
        if data:
            n = type_struct.unpack(data)
            aluno = Student(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11],n[12],n[13],n[14],n[15],n[16],n[17],n[18],n[19],n[20])
            lista.append(aluno)
        else:
            return lista
'''
Funcao que dados o tipo da estrutura(type_struct) o nome de um arquivo e um
Objeto (s) escreve o objetivo em binario no arquivo indicado
'''
def pack_data(type_struct,s,cod):
    # Cria uma tupla do objeto da classe Aluno
    if cod == 1:
        value = (s.inscricao,s.ano,s.cod_municipio,s.municipio,s.cod_uf,s.uf,s.cod_escola,s.idade,s.sexo,s.tp_escola,s.raca,s.p_cn,s.p_ch,s.p_lc,s.p_mt,s.nota_cn,s.nota_ch,s.nota_lc,s.nota_mt,s.nota_redacao,s.renda)
    # Cria uma tupla do Objeto da classe Escola
    elif cod == 2:
        value = (s.id_esc,s.ano,s.codigo,s.nome,s.situacao,s.municipio,s.uf,s.tipo_escola,s.media_cn,s.media_ch,s.media_lc,s.media_mt,s.media_redacao,s.media_geral,s.total_alunos)
    # Cria uma tupla do Objeto da classe Municipio
    elif cod == 3:
        value = (s.id_municipio,s.cod_municipio,s.municipio,s.media_cn,s.media_ch,s.media_lc,s.media_mt,s.media_redacao,s.media_geral,s.total_alunos,s.total_escolas)
    # Cria uma tupla do Objeto da classe Estado
    elif cod == 4:
        value = (s.id_uf,s.cod_uf,s.media_cn,s.media_ch,s.media_lc,s.media_mt,s.media_redacao,s.media_geral,s.total_alunos,s.total_escolas,s.total_municipios)
    # Compacta o a tupla
    bin_value = type_struct.pack(*value)
    return bin_value
