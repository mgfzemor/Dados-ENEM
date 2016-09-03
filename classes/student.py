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

class Student:
    media = 0
    def __init__(self,inscricao,ano,municipio,uf,idade,sexo,st_conclusao,ano_concluiu,tp_escola,in_tp_ensino,raca,nota_cn,nota_ch,nota_lc,nota_mt,nota_redacao,renda):
        self.inscricao = inscricao
        self.ano = ano
        self.municipio = municipio
        self.uf = uf
        self.idade = idade
        self.sexo = sexo
        self.st_conclusao = st_conclusao
        self.ano_concluiu = ano_concluiu
        self.tp_escola = tp_escola
        self.in_tp_ensino = in_tp_ensino
        self.raca = raca
        self.nota_cn = nota_cn
        self.nota_ch = nota_cn
        self.nota_lc = nota_lc
        self.nota_mt = nota_mt
        self.nota_redacao = nota_redacao
        self.renda = renda

    def calc_media(self):
        return ((self.nota_cn + self.nota_ch + self.nota_lc + self.nota_mt + self.nota_redacao)/5)
