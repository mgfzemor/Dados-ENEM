
'''
funcao que compara qualquer atributo da classe student, de acordo com a key escolhida pelo usuario.
a key eh um int, de acordo com a seguinte tabela:

0:    inscricao -> Numero de inscricao
1:    ano -> Ano do Enem
2:    idade -> equ*
3:    ano_concluiu -> Ano de conclusao do Ensino Medio
4:    nota_cn -> Nota da prova de Ciencias da Natureza
5:    nota_ch -> Nota da prova de Ciencias Humanas
6:    nota_lc -> Nota da prova de Linguagens e Codigos
7:    nota_mt -> Nota da prova de Matematica
8:    nota_redacao -> Nota da prova de redacao
9:    renda -> Renda mensal da familia


retornando: 1, se d1>d2.  0, se d1 = d2. -1 se d1<d2
'''

def funcao_cmp(d1,d2,key):
	retorno = 0
	if (key == 0):
		if (d1.inscricao > d2.inscricao):
			retorno = 1
		elif (d1.inscricao == d2.inscricao):
			retorno = 0
		else:
			retorno = -1

	elif (key == 1):
		if (d1.ano > d2.ano):
			retorno = 1
		elif (d1.ano == d2.ano):
			retorno = 0
		else:
			retorno = -1

	elif (key == 2):
		if (d1.idade > d2.idade):
			retorno = 1
		elif (d1.idade == d2.idade):
			retorno = 0
		else:
			retorno = -1

	elif (key == 3):
		if (d1.ano_concluiu > d2.ano_concluiu):
			retorno = 1
		elif (d1.ano_concluiu == d2.ano_concluiu):
			retorno = 0
		else:
			retorno = -1

	elif (key == 4):
		if (d1.nota_cn > d2.nota_cn):
			retorno = 1
		elif (d1.nota_cn == d2.nota_cn):
			retorno = 0
		else:
			retorno = -1

	elif (key == 5):
		if (d1.nota_ch > d2.nota_ch):
			retorno = 1
		elif (d1.nota_ch == d2.nota_ch):
			retorno = 0
		else:
			retorno = -1

	elif (key == 6):
		if (d1.nota_lc > d2.nota_lc):
			retorno = 1
		elif (d1.nota_lc == d2.nota_lc):
			retorno = 0
		else:
			retorno = -1

	elif (key == 7):
		if (d1.nota_mt > d2.nota_mt):
			retorno = 1
		elif (d1.nota_mt == d2.nota_mt):
			retorno = 0
		else:
			retorno = -1

	elif (key == 8):
		if (d1.nota_redacao > d2.nota_redacao):
			retorno = 1
		elif (d1.nota_redacao == d2.nota_redacao):
			retorno = 0
		else:
			retorno = -1

	elif (key == 9):
		if (d1.renda > d2.renda):
			retorno = 1
		elif (d1.renda == d2.renda):
			retorno = 0
		else:
			retorno = -1

	elif (key == 10):
		if (d1.municipio > d2.municipio):
			retorno = 1
		elif (d1.municipio == d2.municipio):
			retorno = 0
		else:
			retorno = -1

	return retorno
