'''
##-----------------------------------------------------------------------------------------
Dicionario de variaveis:
Class:
    Student - Represente a entidade que armazena todos os dados de um dado estudante
Instance variables:
    inscricao -> Numero de inscricao
    ano -> Ano do Enem
    municipio -> Nome do municipio de residencia
    uf -> Sigla da Unidade da Federacao da residencia
    idade -> equ*
    sexo -> equ*
    st_conclusao -> Situacao de conclusao do Ensino Medio
    ano_concluiu -> Ano de conclusao do Ensino Medio
    tp_escola ->  Tipo de escola do Ensino Medio
    in_tp_ensino -> Tipo de instituicao que concluiu ou concluira o Ensino Medio
    raca -> cor/raca
    nota_cn -> Nota da prova de Ciencias da Natureza
    nota_ch -> Nota da prova de Ciencias Humanas
    nota_lc -> Nota da prova de Linguagens e Codigos
    nota_mt -> Nota da prova de Matematica
    nota_redacao -> Nota da prova de redacao
    renda -> Renda mensal da familia

##--------------------------------------------------------------------------------------------
## Mais informacoes consultar o dicionaria de dados.
'''
import ast
class Student:
    media = 0
    #O numero presente ao lado do campo indica a posicao na qual infromacao sera buscada no vetor original
    def __init__(self,inscricao,ano,municipio,uf,idade,sexo,st_conclusao,ano_concluiu,tp_escola,in_tp_ensino,raca,nota_cn,nota_ch,nota_lc,nota_mt,nota_redacao,renda):
        self.inscricao = inscricao #0
        self.ano = ano  #1
        self.municipio = municipio #3
        self.uf = uf #5
        self.idade = idade #15
        self.sexo = sexo #16
        self.st_conclusao = st_conclusao #22
        self.ano_concluiu = ano_concluiu #23
        self.tp_escola = tp_escola #24
        self.in_tp_ensino = in_tp_ensino #25
        self.raca = raca #27
        self.nota_cn = nota_cn #70
        self.nota_ch = nota_ch #71
        self.nota_lc = nota_lc #72
        self.nota_mt = nota_mt #73
        self.nota_redacao = nota_redacao #89
        self.renda = renda #92

    def calc_media(self):
        self.media = (self.nota_cn + self.nota_ch + self.nota_lc + self.nota_mt + self.nota_redacao)/5

class Algoritmo:

    def __init__(self,nome,tempo_n,tempo_c):
        self.nome = nome
        self.tempo_n = tempo_n
        self.tempo_c = tempo_c
