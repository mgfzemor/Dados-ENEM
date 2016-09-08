from classes.student import Student
from sort.sort import  bubbleSort

lista = []
for i in range(10):
	new = Student(10-i,2014,'porto alegre','rs',18,'F',i+3,0,0,0,1,i*100,i*100,i*100,i*100,i*100-50,'E')
	lista.append(new)

for i in lista:
	print i.inscricao,i.nota_redacao,i.renda

bubbleSort(lista,8)
print '----------------------------'
for i in lista:
	print i.inscricao,i.nota_redacao,i.renda


