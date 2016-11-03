# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import struct, ast
from classes.student import *
from sort.trie import *
from busca_escola import busca_escola
from collections import Counter

def gerar_arquivo():
    db_escolas = open('data/2014/out/escolas/db_escolas.bin','rb')
    index_trie_escolas = open('data/2014/out/escolas/index_trie_escola.bin','w')
    escola_struct = struct.Struct('l h l 50s h l l h f f f f f f l')
    while True:
        bin_value = db_escolas.read(escola_struct.size)
        if not bin_value:
            db_escolas.close()
            index_trie_escolas.close()
            break
        else:
            e = escola_struct.unpack(bin_value)
            escola = Escola(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14])
            print escola.nome
            lista_palavras = []
            for palavra in escola.nome.split(" "):
                palavra = palavra.replace("\x00","")
                lista_palavras.append(palavra+'-'+str(escola.codigo))
            for palavra in lista_palavras:
                print palavra
                index_trie_escolas.write(palavra+';')
'''
gerar_arquivo()
'''


def busca_esc(key_string):
    lista_resultados = []
    lista_escolas = []
    lista_out = []
    index_trie = open('data/2014/out/escolas/index_trie_escola.bin','r')
    index = str(index_trie.readlines()).split(";")
    trie = Trie()
    for i in index:
        trie.add(i)
    key = str(key_string)
    key = key.upper()
    key = key.replace("\xc3\xa3","A")
    key = key.split(" ")
    print key
    ''' Se o user informou apenas uma palavra entao retornar lista de resultados sugeridos...'''
    if len(key) == 1:
        ''' Retorna uma lista de prefixos para a palavra em questao'''
        lista_resultados.append(trie.start_with_prefix(key[0]+'-'))
        ''' Se encontrou alguma palavra com prefix entao retorna a lista de sugestoes '''
        if lista_resultados[0]:
            print 'lista de resultado:',lista_resultados
            for resultado in lista_resultados[0]:
                print 'resultado'
                resultado = resultado.split("-")[1]
                lista_escolas.append(busca_escola(resultado))
            for escola in lista_escolas:
                lista_out.append([escola.codigo,escola.nome,escola.uf])
            return [2,lista_out]
        else:
            ''' Nao encontrou nenhuma escola com o prefixo informado '''
            return [-1,key[0].lower()]

    else:
        ''' Caso a busca possua mais palavras'''
        for pal in key:
            pal = pal+'-'
            ''' Encontra as escolas que possuem apenas parte da key informada'''
            lista_resultados.append(trie.start_with_prefix(pal))

        lista_cod = []

        if lista_resultados:
            ''' Separa apenas o codigo das escola encontradas'''
            for resultado in lista_resultados:
                for dado in resultado:
                    dado = dado.split("-")[1]
                    lista_cod.append(dado)

            lista_cod = [ite for ite, it in Counter(lista_cod).most_common(20)]
            print lista_cod,'lista codigo'
            for cod in lista_cod:
                if cod:
                    lista_escolas.append(busca_escola(cod))

            for escola in lista_escolas:
                lista_out.append([escola.codigo,escola.nome,escola.uf])
            if lista_out:
                return [2,lista_out]
            else:
                return [-1,"=("]
