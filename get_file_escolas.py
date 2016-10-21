'''
Programa que gera o arquivo invertido contendo a lista de alunos por escolas.

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
candidato = (000000000001,2014,3548708,'SAO BERNARDO DO CAMPO',35,'SP',21261563,18,'M',1,3,1,1,1,1,536.9,570.2,576.1,478.3,560,'E')
escola = (1,2014,35007237,LANDIA SANTOS BATISTA PROFESSORA,1,35,3515707,2,465.72083346,538.395831426,509.745835622,441.149998347,483.252499771,48)
'''

import struct, ast
from classes.student import *
from sort.sort import *
aluno_struct =  struct.Struct('l h l 25s h 2s l h c h h h h h h f f f f h c')
escola_struct = struct.Struct('l h l 50s h l l h f f f f f f l')

# And Imports ===========================================================

data_in = open('data/2014/out/ENEM.bin','rb')


lista_alunos = []
t = 0 # total de alunos geral
e = 0 # total de alunos cadastrados em escolas

# Criando as estruturas do tipo Aluno
print 'lendo alunos...'
while True:
    data = data_in.read(aluno_struct.size)
    if not data:
        break
    s = aluno_struct.unpack(data)
    aluno = Student(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20])
    if not aluno.cod_escola == 0:
        if aluno.p_ch and aluno.p_cn and aluno.p_lc and aluno.p_mt == 1:
            lista_alunos.append(aluno)
            e+=1
    t += 1
data_in.close()

print 'Ordenando alunos por escola...'
mergeSort(lista_alunos,3)

escola_alunos = open('data/2014/out/escolas/escolas_alunos.txt','w')
file_escolas = open('data/2014/out/escolas/file_escolas.bin','wb')

total = 0
index = 0
old = ''
id_esc = 1

while True:
    if not lista_alunos:
        break
    else:
        media_cn = media_ch = media_lc = media_mt = media_redacao = media_geral = total_alunos = 0
        escola = lista_alunos[0].cod_escola
        e = lista_alunos[0]
        escola = lista_alunos[0].cod_escola
        nova_escola = Escola(id_esc,e.ano,e.cod_escola,'',0,0,0,0,0,0,0,0,0,0,0)
        if old == escola:
            break
        ids_alunos = []
        remove = []
        print escola
        for index,aluno in enumerate(lista_alunos):
            if escola == aluno.cod_escola:
                ids_alunos.append(aluno.inscricao)
                media_cn += aluno.nota_cn
                media_ch += aluno.nota_ch
                media_lc += aluno.nota_lc
                media_mt += aluno.nota_mt
                media_redacao += aluno.nota_redacao
                total_alunos += 1
            else:
                lista_alunos = lista_alunos[index:]
                break
        id_esc += 1
        nova_escola.media_cn = media_cn
        nova_escola.media_ch = media_ch
        nova_escola.media_lc = media_lc
        nova_escola.media_mt = media_mt
        nova_escola.media_redacao = media_redacao
        nova_escola.total_alunos = total_alunos
        n = nova_escola
        value = (n.id_esc,n.ano,n.codigo,n.nome,n.situacao,n.municipio,n.uf,n.tipo_escola,n.media_cn,n.media_ch,n.media_lc,n.media_mt,n.media_redacao,n.media_geral,n.total_alunos)
        bin_value = escola_struct.pack(*value)
        file_escolas.write(bin_value)

        escola_alunos.write(str(escola)+';'+str(ids_alunos)+'\n')
        total += len(ids_alunos)
        old = escola
print total
escola_alunos.close()
file_escolas.close()

###### Procurando nome escola --------
nome_escola = open('data/2014/out/ESCOLAS.csv','r')
file_escola = open('data/2014/out/escolas/file_escolas.bin','rb')
not_escola = open('data/2014/out/escolas/escolas_not_found.txt','w')
db_escolas = open('data/2014/out/escolas/db_escolas.bin','wb')
found, not_found,fim = 1,0,0

while True:
    escola_bin = file_escola.read(escola_struct.size)
    if not escola_bin:
        break
    elif fim == 1:
        break
    else:
        e = escola_struct.unpack(escola_bin)
        escola = Escola(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14])
        while True:
            lin = nome_escola.readline()
            if lin == '':
                print 'fim'
                fim = 1
                break
            lin = lin.split(',')

            cod,nome,situacao,uf,mun,tipo = int(lin[2]),lin[3],lin[4],lin[5],lin[6],lin[7]
            if cod == escola.codigo:
                escola.nome,escola.situacao,escola.uf = nome,int(situacao),int(uf)
                escola.municipio,escola.tipo_escola = int(mun),int(tipo)
                escola.id_esc = found
                found +=1
                # Cria o arquivo que servira como banco de dados dos parametros de uma escola
                values = (escola.id_esc,escola.ano,escola.codigo,escola.nome,escola.situacao,escola.municipio,escola.uf,escola.tipo_escola,escola.media_cn,escola.media_ch,escola.media_lc,escola.media_mt,escola.media_redacao,escola.media_geral,escola.total_alunos)
                print values
                bin_values = escola_struct.pack(*values)
                db_escolas.write(bin_values)
                break
            elif cod > escola.codigo:
                not_escola.write(str(e)+'\n')
                not_found += 1
                break
print found,not_found

nome_escola.close()
file_escola.close()
not_escola.close()
db_escolas.close()
