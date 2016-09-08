from funcao_cmp import funcao_cmp

def insertion_sort(lista):
    for i in range(1,len(lista)):
        chave = lista[i] # elemento escolhido como chave para ser inserido na posicao correta
        j = i-1
        while(j>=0 and chave < lista[j]):
            lista[j+1] = lista[j] # desloca o elemento maior para a direita
            j = j-1
        if(lista[i] != chave): #  Verifica se foi realizada uma troca e escreve a chave na posicao correte
            lista[j+1] = chave # caso contrario a chave ja estava na posicao certa

def shellSort(lista):
    h = 1
    n = len(lista)
    while h > 0:
            for i in range(h, n):
                c = lista[i].nota_redacao
                j = i
                while j >= h and c < lista[j - h].nota_redacao:
                    lista[j].nota_redacao = lista[j - h].nota_redacao
                    j = j - h
                    lista[j].nota_redacao = c
            h = int(h / 2.2)


def teste(key):
	funcao_cmp(list)

#algoritmo bubble sort de ordenamento
def bubbleSort(alist,key):
    #print funcao_cmp(alist[i],alist[i+1],key)
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if funcao_cmp(alist[i],alist[i+1],key) == 1:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


