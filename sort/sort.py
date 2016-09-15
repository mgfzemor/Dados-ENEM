from funcao_cmp import funcao_cmp


# INSERTION SORT =========================================================
def insertion_sort(lista):
    for i in range(1,len(lista)):
        chave = lista[i] # elemento escolhido como chave para ser inserido na posicao correta
        j = i-1
        while(j>=0 and chave < lista[j]):
            lista[j+1] = lista[j] # desloca o elemento maior para a direita
            j = j-1
        if(lista[i] != chave): #  Verifica se foi realizada uma troca e escreve a chave na posicao correte
            lista[j+1] = chave # caso contrario a chave ja estava na posicao certa
# END INSERTION SORT =========================================================


# SHELL SORT ==============================================================
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
# END SHELL SORT ===========================================================


# BUBBLE SORT ==============================================================
def bubbleSort(alist,key):
    #print funcao_cmp(alist[i],alist[i+1],key)
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if funcao_cmp(alist[i],alist[i+1],key) == 1:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
# END BUBBLE SORT ==============================================================


# HEAP SORT ============================================================
def heapsort(lst):

  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)

  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst

def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break
# END HEAP SORT ==========================================================

