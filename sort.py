'''
Programa que executa a analise dos algoritmos implementados, retornando o tempo
de execucao para diferentes tamanhos de entrada de dados.
dicionario para a variavel 'algoritmos'
1- insertionSort    3- shellSort   5- quickSort  7- heapSort
2- insertionSortBB  4- bubbleSort  6- mergeSort  8- radixSort
'''
# Imports
from classes.student import Student
from classes.student import Algoritmo
from sort.sort import *
import time
import struct
type_struct = struct.Struct('l h 25s 2s h c h h h h h f f f f h c')
# And Imports ===========================================================

def write_file(alg,kind,qtd,time):
    resultado.write(alg+', '+kind+', '+str(qtd)+', '+str(int((fim-ini)*100))+'.\n')

ini =0
fim =0
resultado = open('resultados_team_quarks.txt','w')
chart_arq_n = open('data/chart_list_n.txt','w')
chart_arq_c = open('data/chart_list_c.txt','w')

ISBL = Algoritmo('ISBL',[],[])
ISBB = Algoritmo('ISBB',[],[])
SHST = Algoritmo('SHST',[],[])
BBST = Algoritmo('BBST',[],[])
QSRM = Algoritmo('QSRM',[],[])
MGST = Algoritmo('MGST',[],[])
HPST = Algoritmo('HPST',[],[])
RMSD = Algoritmo('RMSD',[],[])

print 'Analysis of algorithms...'
quantidade = [100,10000,1000000] # Adicionar 1.000.000 apenas localmente
algoritmos = [1,2,3,4,5,6,7,8] #
for algoritmo in algoritmos:
    print algoritmo,'---------'
    for qtd in quantidade:
        print '->',qtd
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

        #if qtd == 100:
        #    for i in lista_n:
        #        print i.nota_redacao,i.inscricao,i.municipio
        print '-------------------------------------'
        if algoritmo == 1:
            ini = time.time()
            insertionSort(lista_n,8)
            fim = time.time()
            write_file('ISBL','numerico',qtd,(fim-ini))
            ISBL.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            insertionSort(lista_c,10)
            fim = time.time()
            write_file('ISBL','categorico',qtd,(fim-ini))
            ISBL.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==2:
            ini = time.time()
            lista_n = insertionSortBB(lista_n,8)
            fim = time.time()
            write_file('ISBB','numerico',qtd,(fim-ini))
            ISBB.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            lista_c = insertionSortBB(lista_c,10)
            fim = time.time()
            write_file('ISBB','categorico',qtd,(fim-ini))
            ISBB.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==3:
            ini = time.time()
            shellSort(lista_n,8)
            fim = time.time()
            write_file('SHST','numerico',qtd,(fim-ini))
            SHST.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            shellSort(lista_c,10)
            fim = time.time()
            write_file('SHST','categorico',qtd,(fim-ini))
            SHST.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==4:
            ini = time.time()
            bubbleSort(lista_n,8)
            fim = time.time()
            write_file('BBST','numerico',qtd,(fim-ini))
            BBST.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            bubbleSort(lista_c,10)
            fim = time.time()
            write_file('BBST','categorico',qtd,(fim-ini))
            BBST.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==5:
            ini = time.time()
            quickSort(lista_n,8)
            fim = time.time()
            write_file('QSRM','numerico',qtd,(fim-ini))
            QSRM.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            quickSort(lista_c,10)
            fim = time.time()
            write_file('QSRM','categorico',qtd,(fim-ini))
            QSRM.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==6:
            ini = time.time()
            mergeSort(lista_n,8)
            fim = time.time()
            write_file('MGST','numerico',qtd,(fim-ini))
            MGST.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            mergeSort(lista_c,10)
            fim = time.time()
            write_file('MGST','categorico',qtd,(fim-ini))
            MGST.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==7:
            ini = time.time()
            heapSort(lista_n,8)
            fim = time.time()
            write_file('HPST','numerico',qtd,(fim-ini))
            HPST.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            heapSort(lista_c,10)
            fim = time.time()
            write_file('HPST','categorico',qtd,(fim-ini))
            HPST.tempo_c.append(int((fim-ini)*100))

        elif algoritmo ==8:
            ini = time.time()
            lista_n = radixSort(lista_n,8)
            fim = time.time()
            write_file('RMSD','numerico',qtd,(fim-ini))
            RMSD.tempo_n.append(int((fim-ini)*100))

            ini = time.time()
            lista_c = radixSort(lista_c,10)
            fim = time.time()
            write_file('RMSD','categorico',qtd,(fim-ini))
            RMSD.tempo_c.append(int((fim-ini)*100))


        #if qtd == 100:
        #    for j in lista_n:
        #        print j.nota_redacao,j.inscricao,j.municipio

chart_list = [ISBL,ISBB,SHST,BBST,QSRM,MGST,HPST,RMSD]

for alg in chart_list:
    chart_arq_n.write(alg.nome+','+str(alg.tempo_n)+'\n')
    chart_arq_c.write(alg.nome+','+str(alg.tempo_c)+'\n')
