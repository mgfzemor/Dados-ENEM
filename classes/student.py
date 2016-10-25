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
import ast,decimal
class Student:
    media = 0
    # O numero presente ao lado do campo indica a posicao na qual infromacao sera buscada no vetor original
    def __init__(self,inscricao,ano,cod_municipio,municipio,cod_uf,uf,cod_escola,idade,sexo,tp_escola,raca,p_cn,p_ch,p_lc,p_mt,nota_cn,nota_ch,nota_lc,nota_mt,nota_redacao,renda):
        self.inscricao = inscricao #0
        self.ano = ano  #1
        self.cod_municipio = cod_municipio #2
        self.municipio = municipio #3
        self.cod_uf = cod_uf  #4
        self.uf = uf #5
        self.cod_escola = cod_escola #7
        self.idade = idade #15
        self.sexo = sexo #16
        self.tp_escola = tp_escola #24
        self.raca = raca #27
        self.p_cn = p_cn #62
        self.p_ch = p_ch #63
        self.p_lc = p_lc #64
        self.p_mt = p_mt #65
        self.nota_cn = round(decimal.Decimal(nota_cn),1) #70
        self.nota_ch = round(decimal.Decimal(nota_ch),1) #71
        self.nota_lc = round(decimal.Decimal(nota_lc),1) #72
        self.nota_mt = round(decimal.Decimal(nota_mt),1) #73
        self.nota_redacao = round(decimal.Decimal(nota_redacao),1) #89
        self.renda = renda #92

    def calc_media(self):
        self.media = round(decimal.Decimal((self.nota_cn + self.nota_ch + self.nota_lc + self.nota_mt + self.nota_redacao)/5),1)

class Escola:
    def __init__(self,id_esc,ano,codigo,nome,situacao,municipio,uf,tipo_escola,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos):
        self.id_esc = id_esc
        self.ano = ano
        self.codigo = codigo
        self.nome = nome
        self.situacao = situacao
        self.municipio = municipio
        self.uf = uf
        self.tipo_escola = tipo_escola
        self.media_cn = media_cn
        self.media_ch = media_ch
        self.media_lc = media_lc
        self.media_mt = media_mt
        self.media_redacao = media_redacao
        self.media_geral = media_geral
        self.total_alunos = total_alunos

class Municipio:
    def __init__(sefl,id_municipio,cod_municipio,ano,municipio,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos,total_escolas):
        self.id_municipio = id_municipio
        self.cod_municipio = cod_municipio
        self.ano = ano
        self.municipio = municipio
        self.media_cn = media_cn
        self.media_ch = media_ch
        self.media_lc = media_lc
        self.media_mt = media_mt
        self.media_redacao = media_redacao
        self.media_geral = media_geral
        self.total_alunos = total_alunos
        self.total_escolas = total_escolas

class Estado:
    def __init(self,id_uf,cod_uf,media_cn,media_ch,media_lc,media_mt,media_redacao,media_geral,total_alunos,total_escolas,total_municipios):
        self.id_uf = id_uf
        self.cod_uf = cod_uf
        self.media_cn = media_cn
        self.media_ch = media_ch
        self.media_lc = media_lc
        self.media_mt = media_mt
        self.media_redacao = media_redacao
        self.media_geral = media_geral
        self.total_alunos = total_alunos
        self.total_escolas = total_escolas
        self.total_municipios = total_municipios


class Algoritmo:
    def __init__(self,nome,tempo_n,tempo_c):
        self.nome = nome
        self.tempo_n = tempo_n
        self.tempo_c = tempo_c
