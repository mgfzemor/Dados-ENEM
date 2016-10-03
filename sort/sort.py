from funcao_cmp import funcao_cmp
from atributo_radix import atributo_radix
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

def binary_search(A, value, start, end,key):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if funcao_cmp(A[start], value,key) == 1:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than value
    if start > end:
        return start

    mid = (start+end)/2
    if funcao_cmp(A[mid], value, key) == -1:
        return binary_search(A, value, mid+1, end,key)
    elif funcao_cmp(A[mid], value,key) == 1:
        return binary_search(A, value, start, mid-1,key)
    else:
        return mid

def insertionSortBB(A,key):
    for i in xrange(1, len(A)):
        value = A[i]
        j = binary_search(A, value, 0, i-1,key)
        A = A[:j] + [value] + A[j:i] + A[i+1:]
    return A

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
    if (key == 10):
        return radix_String(lista)
    else:
        return radix_num (lista,key)

def radix_num(a,key):
    r = 10
    maxLen = 11
    for x in range(maxLen):
        bins = [[] for i in range(r+9)]
        for y in a:
            if(atributo_radix(y,key)>=0):
                bins[(atributo_radix(y,key)/10**x)%r+9].append(y)
            else:
                bins[(atributo_radix(y,key)/10**x)%r].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

# Radix sort for variable length strings
def radix_String(lista):
    maxLen = -1
    for aluno in lista: # Find longest string
        aluno.municipio = aluno.municipio.replace("\x00","")
        aluno.municipio = aluno.municipio.replace(" ","")
        strLen = len(aluno.municipio)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('A') - 1; # First character code
    oz = ord('Z') - 1; # Last character code
    n = oz - oa + 2; # Number of buckets (+empty character)
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, maxLen)):
        for aluno in lista:
            index = 0 # Assume "empty" character
            if position < len(aluno.municipio): # Might be within length
                index = ord(aluno.municipio[position]) - oa
            buckets[index].append(aluno) # Add to bucket
        del lista[:]
        for bucket in buckets: # Reassemble lista in new order
            lista.extend(bucket)
            del bucket[:]
    return lista
# END RADIX SORT ==========================================================
