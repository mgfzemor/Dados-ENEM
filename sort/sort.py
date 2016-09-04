
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
                c = lista[i]
                j = i
                while j >= h and c < lista[j - h]:
                    lista[j] = lista[j - h]
                    j = j - h
                    lista[j] = c
            h = int(h / 2.2)
