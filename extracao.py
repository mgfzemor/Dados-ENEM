'''
Programa que gera dois arquivos com 1.000.000 elementos ordenados de forma descrescente.
Como o programa tem como objetivo apenas gerar arquivos ordenados inversamente sera utilizada
a funcao de sort ja implementada no python.
Recebe como entrada o data.bin contendo todas as informacoes
'''
# Imports
from classes.student import Student
from sort.sort import shellSort
import struct
type_struct = struct.Struct('l h 25s 2s h c h h h h h f f f f h c')
# And Imports ===========================================================
numerico = open('data/numerico.bin','wb')
categorico = open('data/categorico.bin','wb')
data_in = open('data/data.bin','rb')

quantidade = [100000]

for qtd in quantidade:
    l = []
    for i in range(qtd):
        data = data_in.read(type_struct.size)
        s = type_struct.unpack(data)
        new = (s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16])
        #print new.nota_redacao
        l.append(new)

def getKeyNum(item):
    return item[15]

def getKeyCat(item):
    return item[2]
print 'Ordenando numerico...'
# Ordenando o arquivo numerico pela chave Nota da redacao
l.sort(key=getKeyNum,reverse=True)

for i in l:
    data_bin = type_struct.pack(*i)
    numerico.write(data_bin)
print 'ok'
print 'Ordenando categorico...'
# Ordenando o arquivo numerico pela chave Municipio
l.sort(key=getKeyCat,reverse=True)

for j in l:
    data_bin = type_struct.pack(*j)
    categorico.write(data_bin)
print 'ok'
