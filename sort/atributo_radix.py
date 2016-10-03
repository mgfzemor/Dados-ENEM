'''
funcao auxiliar da funcao radixSort, retornando apenas o campo relacionado a uma key

0:    inscricao -> Numero de inscricao
1:    ano -> Ano do Enem
2:    idade -> equ*
3:    ano_concluiu -> Ano de conclusao do Ensino Medio
4:    nota_cn -> Nota da prova de Ciencias da Natureza
5:    nota_ch -> Nota da prova de Ciencias Humanas
6:    nota_lc -> Nota da prova de Linguagens e Codigos
7:    nota_mt -> Nota da prova de Matematica
8:    nota_redacao -> Nota da prova de redacao
9:    renda -> Renda mensal da famila
10:   municipio -> Municipio do candidato
'''

def atributo_radix (elemento, key):
    retorno = 0
    if (key == 0):
        retorno = elemento.inscricao

    elif (key == 1):
        retorno = elemento.ano

    elif(key == 2):
        retorno = elemento.idade
    elif (key == 3):
        retorno = elemento.ano_concluiu

    elif (key == 4):
		retorno = elemento.nota_cn

    elif (key == 5):
		retorno = elemento.nota_ch

    elif (key == 6):
		retorno = elemento.nota_lc

    elif (key == 7):
		retorno = elemento.nota_mt

    elif (key == 8):
		retorno = elemento.nota_redacao

    elif (key == 9):
		retorno = elemento.renda

    elif (key == 10):
        retorno = elemento.municipio

    return retorno
