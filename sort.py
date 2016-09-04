'''
teste
'''
# Imports
from classes.student import Student
from sort.sort import shellSort
import time
import struct
type_struct = struct.Struct('l h 25s 2s h c h h h h h f f f f h c')
# And Imports ===========================================================

data_in = open('data/data.bin','rb')

ini =0
fim =0

print 'Analysis of shellSort'
quantidade = [500,1000,5000,10000,20000,25000,30000,40000,50000,75000,1000000]

for qtd in quantidade:
    l = []
    for i in range(qtd):
        data = data_in.read(type_struct.size)
        s = type_struct.unpack(data)
        new = Student(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16])
        #print new.nota_redacao
        l.append(new)

    ini = time.time()
    shellSort(l)
    fim = time.time()
    print '================================='
    print '--',qtd,'--'
    print 'Aleaorio -> tempo:',fim - ini
    ini=0
    fim=0
    ini = time.time()
    shellSort(l)
    fim = time.time()
    print 'Ordenado -> tempo:',fim - ini
