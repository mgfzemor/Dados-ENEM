'''
Programa que executa a analise dos algoritmos implementados, retornando o tempo
de execucao para diferentes tamanhos de entrada de dados.
dicionario para a variavel 'algoritmos'
1- insertionSort    3- shellSort   5- quickSort  7- heapSort
2- insertionSortBB  4- bubbleSort  6- mergeSort  8- radixSort
'''
# Imports
from classes.student import Student
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

print 'Analysis of algorithms...'
quantidade = [100,1000,10000] # Adicionar 1.000.000 apenas localmente
algoritmos = [1,3,4,6,7] #
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
            #for i in lista_n:
                #print i.nota_redacao,i.inscricao,i.municipio
        #print '-------------------------------------'
        if algoritmo == 1:
            ini = time.time()
            insertionSort(lista_n,8)
            fim = time.time()
            write_file('ISBL','numerico',qtd,(fim-ini))

            ini = time.time()
            insertionSort(lista_c,10)
            fim = time.time()
            write_file('ISBL','categorico',qtd,(fim-ini))

        elif algoritmo ==2:
            ini = time.time()
            insertionSortBB(lista_n,8)
            fim = time.time()
            write_file('ISBB','numerico',qtd,(fim-ini))

            ini = time.time()
            insertionSortBB(lista_c,10)
            fim = time.time()
            write_file('ISBB','categorico',qtd,(fim-ini))

        elif algoritmo ==3:
            ini = time.time()
            shellSort(lista_n,8)
            fim = time.time()
            write_file('SHST','numerico',qtd,(fim-ini))

            ini = time.time()
            shellSort(lista_c,10)
            fim = time.time()
            write_file('SHST','categorico',qtd,(fim-ini))

        elif algoritmo ==4:
            ini = time.time()
            bubbleSort(lista_n,8)
            fim = time.time()
            write_file('BBST','numerico',qtd,(fim-ini))

            ini = time.time()
            bubbleSort(lista_c,10)
            fim = time.time()
            write_file('BBST','categorico',qtd,(fim-ini))

        elif algoritmo ==5:
            ini = time.time()
            quickSort(lista_n,8)
            fim = time.time()
            write_file('QSRM','numerico',HPSTqtd,(fim-ini))

            ini = time.time()
            quickSort(lista_c,10)
            fim = time.time()
            write_file('QSRM','categorico',qtd,(fim-ini))

        elif algoritmo ==6:
            ini = time.time()
            mergeSort(lista_n,8)
            fim = time.time()
            write_file('MGST','numerico',qtd,(fim-ini))


            ini = time.time()
            mergeSort(lista_c,10)
            fim = time.time()
            write_file('MGST','categorico',qtd,(fim-ini))

        elif algoritmo ==7:
            ini = time.time()
            heapSort(lista_n,8)
            fim = time.time()
            write_file('HPST','numerico',qtd,(fim-ini))

            ini = time.time()
            heapSort(lista_c,10)
            fim = time.time()
            write_file('HPST','categorico',qtd,(fim-ini))

        elif algoritmo ==8:
            ini = time.time()
            radixSort(lista_n,8)
            fim = time.time()
            write_file('RMSD','numerico',qtd,(fim-ini))

            ini = time.time()
            radixSort(lista_c,10)
            fim = time.time()
            write_file('RMSD','numerico',qtd,(fim-ini))




        #if qtd == 100:
            #for j in lista_n:
                #print j.nota_redacao,j.inscricao,j.municipio
