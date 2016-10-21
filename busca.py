'''
Dado o numero de inscricao de um aluno retorna seus dados
'''
import struct
from classes.student import *
from math import sqrt

def busca_inscricao(inscricao):
    inscricao = int(inscricao)
    desloc = inscricao - 140000000001
    aluno_struct =  struct.Struct('l h l 25s h 2s l h c h h h h h h f f f f h c')

    db_aluno = open('data/2014/out/db_aluno.bin','rb')

    db_aluno.seek(-(aluno_struct.size),2)
    bin_value = db_aluno.read(aluno_struct.size)
    aluno = aluno_struct.unpack(bin_value)
    pos =  db_aluno.tell()
    # Salva o maior deslocamento que pode ser feito dentro do arquivo
    desloc_max = pos/aluno_struct.size
    # Salva maior id registrado
    insc_max = aluno[0]
    # Verifica se o numero da incricao esta fora dos limites cadastrados
    if inscricao > insc_max or desloc < 0:
        found = 0
    else:
         # Se o desloc for maior que o desloc_max entao a busca pela chave eh feita
        # final para o inicio ate que seja encontrado
        if desloc > desloc_max:
            des = 1
            while True:
                db_aluno.seek(-(des*aluno_struct.size),2)
                bin_value = db_aluno.read(aluno_struct.size)
                aluno = aluno_struct.unpack(bin_value)
                chave = aluno[0]

                if inscricao == chave:
                    found = 1
                    break
                elif inscricao > chave:
                    break
                else:
                    des += 1
        else:
            while True:
                db_aluno.seek((desloc*aluno_struct.size))
                bin_value = db_aluno.read(aluno_struct.size)
                aluno = aluno_struct.unpack(bin_value)
                if inscricao == aluno[0]:
                    found = 1
                    break
                elif inscricao > aluno[0]:
                    break
                else:
                    desloc -= 1
    aluno = list(aluno)
    return [found,aluno]

# Dado um codigo de uma escola retorna uma lista de alunos pertencentes a mesma
def busca_alunos_por_escola(cod_escola):
    escola_alunos = open('data/2014/out/escolas/escolas_alunos.txt','r')
    alunos = []
    while True:
        escola = escola_alunos.readline()
        if not escola:
            print 'not found escola'
            break
        else:
            escola = escola.split(';')
            # Removendo chars inuteis
            escola[1] = escola[1].replace("[","")
            escola[1] = escola[1].replace("]","")
            escola[1] = escola[1].replace("\n","")
            escola[1] = escola[1].replace(" ","")

            lista_alunos = escola[1].split(',')
            escola = escola[0]

            if cod_escola == int(escola):
                media_escola = 0
                graph_notas = []
                for aluno in lista_alunos:
                    out = busca_inscricao(aluno)
                    if out[0] == 1:
                        i = out[1]
                        student = Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20])
                        student.calc_media()
                        media_escola += student.media
                        graph_notas.append(student.media)
                        alunos.append(student)
                return [alunos,media_escola,graph_notas]

def gera_grafico(aluno,lista):
    print aluno
    print lista
    num_colunas = round(sqrt(len(lista)))
    num_colunas = int(num_colunas)
    if num_colunas == 0:
        num_colunas = 1
    amp_classe = round((max(lista)-min(lista))/num_colunas)
    print amp_classe
    print num_colunas,amp_classe

    colunas = []
    lista_lim_classe = []
    mi =  min(lista)
    ma = max(lista)
    print mi,'valor minimo'
    print ma,'valor maximo'
    for i in range(0,num_colunas+1):
        print i
        colunas = colunas + [0]
        lista_lim_classe = lista_lim_classe + [0]
        lista_lim_classe[i] = (i*amp_classe)+mi
    lista_lim_classe[i] = ma


    for i in lista:
        if (i > lista_lim_classe[num_colunas]):
            colunas[num_colunas-1]+=1
        else:
            for j,nota in enumerate(lista_lim_classe):
                if (i <= nota):
                    colunas[j]+=1
                    break

    if (aluno > lista_lim_classe[num_colunas]):
        coluna_aluno = num_colunas
    else:
        for j,nota in enumerate(lista_lim_classe):
            if (aluno <= nota):
                coluna_aluno = j
                break

    retorno = []
    retorno = [coluna_aluno,lista_lim_classe,colunas]
    return retorno
