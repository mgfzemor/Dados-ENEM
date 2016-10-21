from busca import *
import decimal,struct
from classes.student import *
from sort.sort import *

sigla_to_estado = {'AC': 'Acre', 'AP': 'Amapa', 'AM': 'Amazonas','BA': 'Bahia', 'CE': 'Ceara',
'DF': 'Distrito Federal', 'ES': 'Espirito Santo', 'GO': 'Goias','MA': 'Maranhao', 'MT': 'Mato Grosso',
'MS': 'Mato Grosso do Sul','MG': 'Minas Gerais','PA': 'Para','PB': 'Paraiba','PR': 'Parana',
'PE': 'Pernambuco','PI': 'Piaui','RJ': 'Rio de Janeiro','RN': 'Rio Grande do Norte','RS': 'Rio Grande do Sul',
'RO': 'Rondonia','RR': 'Roraima','SC': 'Santa Catarina','SP': 'Sao Paulo','SE': 'Sergipe','TO': 'Tocantins'}

def make_page_aluno(inscricao):
    out = busca_inscricao(inscricao)
    found = out[0]
    a = out[1]
    aluno = Student(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19],a[20])
    aluno.uf = sigla_to_estado[aluno.uf]
    aluno.calc_media()
    escola = ''
    cod_esc_aluno = 0
    #se a escola nao foi informada recebe 'nao informado'
    if aluno.cod_escola ==0:
        aluno.cod_escola = 'Nao informado'
    else:
        db_escolas = open('data/2014/out/escolas/db_escolas.bin','rb')
        escola_struct = struct.Struct('l h l 50s h l l h f f f f f f l')
        i=0
        while True:
            bin_value = db_escolas.read(escola_struct.size)
            if not bin_value:
                aluno.cod_escola= str(aluno.cod_escola)+'- Escola nao encontrada'
                escola = None
                break
            else:
                # cod_esc_aluno salva o codigo da escola para comparar com outros alunos da escola
                cod_esc_aluno = aluno.cod_escola
                e = escola_struct.unpack(bin_value)
                escola = Escola(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14])
                if aluno.cod_escola == escola.codigo:
                    escola.media_cn = round(decimal.Decimal( escola.media_cn/escola.total_alunos),1)
                    escola.media_ch = round(decimal.Decimal( escola.media_ch/escola.total_alunos),1)
                    escola.media_lc = round(decimal.Decimal( escola.media_lc/escola.total_alunos),1)
                    escola.media_mt = round(decimal.Decimal( escola.media_mt/escola.total_alunos),1)
                    escola.media_redacao = round(decimal.Decimal( escola.media_redacao/escola.total_alunos),1)
                    aluno.cod_escola = escola.nome
                    # (1-Federal | 2-Estadual | 3-Municipal | 4-Privada)
                    if escola.tipo_escola == 1:
                        escola.tipo_escola = 'Federal'
                    elif escola.tipo_escola == 2:
                        escola.tipo_escola = 'Estadual'
                    elif escola.tipo_escola == 3:
                        escola.tipo_escola = 'Municipal'
                    elif escola.tipo_escola == 4:
                        escola.tipo_escola = 'Privada'
                    else:
                        escola.tipo_escola = 'NI'
                    print 'found'
                    break

    #substitui o codigo de raca pela string com a raca
    if aluno.raca == 0:
        aluno.raca = 'Nao informado'
    elif aluno.raca == 1:
        aluno.raca = 'Branco'
    elif aluno.raca == 2:
        aluno.raca = 'Preto'
    elif aluno.raca == 3:
        aluno.raca = 'Parda'
    elif aluno.raca == 4:
        aluno.raca = 'Amarela'
    elif aluno.raca == 5:
        aluno.raca = 'Indigena'

    esc_pos = -1
    graph = []
    if cod_esc_aluno != 0:
        out = busca_alunos_por_escola(cod_esc_aluno)
        lista_alunos_escola = out[0]
        media_escola = out[1]
        graph_notas = out[2]
        escola.media_geral = media_escola/escola.total_alunos

        mergeSort(lista_alunos_escola,11)
        lista_alunos_escola = reversed(lista_alunos_escola)
        graph = gera_grafico(aluno.media,graph_notas)

        for esc_pos,i in enumerate(lista_alunos_escola):
            if i.inscricao == aluno.inscricao:
                esc_pos+=1
                break

    return [found,aluno,escola,esc_pos,graph]
