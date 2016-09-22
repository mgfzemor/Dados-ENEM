'''
teste
'''
# Imports
from classes.student import Student
from sort.sort import *
import time
import struct
type_struct = struct.Struct('l h 25s 2s h c h h h h h f f f f h c')
# And Imports ===========================================================

ini =0
fim =0

print 'Analysis of algorithms...'
quantidade = [25,100,1000,10000,100000 ] # Adicionar 1.000.000 apenas localmente

for qtd in quantidade:
    numerico = open('data/numerico.bin','rb')
    categorico = open('data/categorico.bin','rb')
    lista_n = []
    lista_c = []
    for i in range(qtd):
        data_numumerico = numerico.read(type_struct.size) # Le o numero de bytes de uma Struct
        data_categorico = categorico.read(type_struct.size)
        n = type_struct.unpack(data_numumerico) # Descompacta os dados binarios
        c = type_struct.unpack(data_categorico)
        # Cria um novo Objeto
        student_n = Student(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11],n[12],n[13],n[14],n[15],n[16])
        student_c = Student(n[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16])
        # Add para a lista
        lista_n.append(student_n)
        lista_c.append(student_c)

    numerico.close()
    categorico.close()

    #if qtd == 25:
        #for i in lista_c:
            #print i.nota_redacao,i.inscricao,i.municipio

    ini = time.time()
    insertion_sort(lista_n,8)
    fim = time.time()
    print 'SHST, numerico,',qtd,',',int((fim-ini)*100),'ms'

    ini = time.time()
    insertion_sort(lista_c,10)
    fim = time.time()
    print 'SHST, categorico,',qtd,',',int((fim-ini)*100),'ms'

    #if qtd == 25:
        #for j in lista_c:
            #print j.nota_redacao,j.inscricao,j.municipio
