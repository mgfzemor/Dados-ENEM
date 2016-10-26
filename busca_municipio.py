from pack.pack import *
import struct

def busca_mun(cod):
    index_municipio = open('data/2014/out/municipio/index_municipio.bin','rb')
    while True:
        data = index_municipio.read(index_municipio_struct.size)
        if data:
            index = index_municipio_struct.unpack(data)
            print index
            if index[1] == cod:
                municipio_alunos = open('data/2014/out/municipio/municipio_alunos.bin','rb')
                municipio_alunos.seek(index[2])
                data = municipio_alunos.read(lista_alunos_struct.size)
                index = lista_alunos_struct.unpack(data)
                print index
                break
        else:
            break



busca_mun(2700102)
