from funcao_cmp import funcao_cmp
import random


# INSERTION SORT =========================================================
def insertionSort(lista,key):
    for i in range(1,len(lista)):
        chave = lista[i] # elemento escolhido como chave para ser inserido na posicao correta
        j = i-1
        while(j>=0 and funcao_cmp(chave,lista[j],key) == -1):
            lista[j+1] = lista[j] # desloca o elemento maior para a direita
            j = j-1
        if(lista[i] != chave): #  Verifica se foi realizada uma troca e escreve a chave na posicao correte
            lista[j+1] = chave # caso contrario a chave ja estava na posicao certa
# END INSERTION SORT =========================================================

# INSERTION SORT BUSCA BINARIA =========================================================

def insertionSortBB(lista,key):
    return 0

# END INSERTION SORT BUSCA BINARIA =========================================================

# SHELL SORT ==============================================================
def shellSort(lista,key):
    h = 1
    n = len(lista)
    while h > 0:
            for i in range(h, n):
                c = lista[i]
                j = i
                while j >= h and funcao_cmp(c,lista[j - h],key) == -1:
                    lista[j] = lista[j - h]
                    j = j - h
                    lista[j] = c
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


# QUICK SORT ==============================================================
def quickSort(lista,key):
    a = 0
    b = len(lista)-1
    quick_sort_iterative(lista,a,b,key)
    #return lista

def quick_sort_iterative(list_, left, right,key):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left,right))

    #Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_,left,right,key)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))

def partition(list_, left, right,key):
    """
    Partition method
    """
    #Pivot first element in the array

    posicao_aleatoria = random.choice(range(left,right))
    list_[left], list_[posicao_aleatoria] = list_[posicao_aleatoria], list_[left]
    piv = list_[left]
    i = left + 1
    j = right

    while 1:
        while i <= j  and funcao_cmp(list_[i],piv,key)<=0:
            i +=1
        while j >= i and funcao_cmp(list_[j],piv,key)>=0:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j
# END QUICK SORT ==============================================================

# HEAP SORT ============================================================
def heapSort(lst,key):
    for start in range((len(lst)-2)/2, -1, -1):
        siftdown(lst, start, len(lst)-1,key)

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1,key)
    return lst

def siftdown(lst, start, end,key):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and funcao_cmp(lst[child], lst[child + 1],key) == -1:
            child += 1
        if funcao_cmp(lst[root], lst[child],key) == -1:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break
# END HEAP SORT ==========================================================


# MERGE SORT ============================================================
def mergeSort(alist,key):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,key)
        mergeSort(righthalf,key)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if funcao_cmp(lefthalf[i],righthalf[j],key) == -1:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
# END MERGE SORT ==========================================================

# RADIX SORT ==========================================================
def radixSort(lista,key):
    return 0
# END RADIX SORT ==========================================================
