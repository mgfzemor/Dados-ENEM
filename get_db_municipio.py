from pack.pack import *
from sort.sort import *
import struct
estados = ['AC','AL','AP', 'AM','BA', 'CE','DF', 'ES', 'GO','MA', 'MT','MS','MG','PA','PB','PR',
'PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

for uf in estados:
    db = 'data/2014/estados/'+uf+'.bin'
    print 'reading file '+uf+'...'
    alunos = unpack_data(aluno_struct,db)
    print 'ok!'


    mergeSort(alunos,12)

    for aluno in alunos:
        print aluno.cod_municipio,aluno.p_cn, aluno.p_ch, aluno.p_lc, aluno.p_mt
    print '--------'

    db_municipio = open('data/2014/out/municipio/db_municipio.bin','a+')
    municipio_alunos = open('data/2014/out/municipio/municipio_alunos.bin','a+')
    municipio_escolas = open('data/2014/out/municipio/municipio_escolas.bin','a+')
    index_municipio = open('data/2014/out/municipio/index_municipio.bin','a+')
    if uf == 'AC':
        id_mun = 1
        old = ''
        offset_aluno = 0
        offset_escola = 0
        prox_offset_aluno = 0
        prox_offset_escola = 0
    while True:
        if not alunos:
            break
        else:
            validos = media_cn = media_ch = media_lc = media_mt = media_redacao = media_geral = total_alunos= total_escolas = 0

            lista_escolas = []
            lista_alunos = []
            aluno = alunos[0]
            municipio_cod = aluno.cod_municipio
            novo_municipio = Municipio(id_mun,aluno.cod_municipio,aluno.municipio,0,0,0,0,0,0,total_alunos,total_escolas)
            if old == municipio_cod:
                break
            for index,aluno in enumerate(alunos):
                if aluno.cod_municipio == municipio_cod:
                    if aluno.p_cn and aluno.p_ch and aluno.p_lc and aluno.p_mt:
                        validos += 1
                        media_cn += aluno.nota_cn
                        media_ch += aluno.nota_ch
                        media_lc += aluno.nota_lc
                        media_mt += aluno.nota_mt
                        media_redacao += aluno.nota_redacao
                        aluno.calc_media()
                        media_geral += aluno.media
                        if aluno.cod_escola not in lista_escolas and aluno.cod_escola:
                            lista_escolas.append(aluno.cod_escola)
                            total_escolas +=1
                    total_alunos += 1
                    lista_alunos.append(aluno.inscricao)
                else:
                    alunos = alunos[index:]
                    break
            if total_alunos:
                id_mun += 1
                if validos:
                    novo_municipio.media_cn = media_cn/validos
                    novo_municipio.media_ch = media_ch/validos
                    novo_municipio.media_lc = media_lc/validos
                    novo_municipio.media_mt = media_mt/validos
                    novo_municipio.media_geral = media_geral/validos
                    if media_redacao != 0:
                        print media_redacao,'redacao',total_alunos,'total alunos',validos,'validos'
                        novo_municipio.media_redacao = media_redacao/validos
                        print 'media_red',novo_municipio.media_redacao

                novo_municipio.total_alunos = total_alunos
                novo_municipio.total_escolas = total_escolas
                s = novo_municipio
                # Insere o novo_municipio no banco de dados
                bin_value = pack_data(municipio_struct,novo_municipio,3)
                db_municipio.write(bin_value)
                '''
                ============== Cria o arquivo binario com a lista de alunos do municipio =================
                '''
                if lista_alunos:
                    value = (s.id_municipio,s.cod_municipio,total_alunos)
                    bin_value = lista_alunos_struct.pack(*value)
                    municipio_alunos.write(bin_value)
                    prox_offset_aluno += lista_alunos_struct.size
                    for index,aluno in enumerate(lista_alunos):
                        value = (index,aluno)
                        bin_value = int_struct.pack(*value)
                        municipio_alunos.write(bin_value)
                        prox_offset_aluno += int_struct.size
                    print offset_aluno,'offset aluno'
                '''
                ============= Cria o arquivo binario com a lista de escolas do municipio =================
                '''
                if lista_escolas:
                    value = (s.id_municipio,s.cod_municipio,total_escolas)
                    bin_value = lista_escolas_struct.pack(*value)
                    municipio_escolas.write(bin_value)
                    prox_offset_escola += lista_escolas_struct.size
                    for index,escola in enumerate(lista_escolas):
                        value = (index,escola)
                        bin_value = int_struct.pack(*value)
                        municipio_escolas.write(bin_value)
                        prox_offset_escola += int_struct.size
                    print offset_escola,'offset escola'

                '''
                ============= Cria o arquivo de indeces que realiza a busca de um municipio ================
                '''
                if not lista_alunos:
                    offset_aluno = -1
                if not lista_escolas:
                    offset_escola = -1
                value = (s.id_municipio,s.cod_municipio,offset_aluno,offset_escola)
                bin_value = index_municipio_struct.pack(*value)
                index_municipio.write(bin_value)

                offset_aluno = prox_offset_aluno
                offset_escola = prox_offset_escola

                print lista_escolas,'escolas'
                print lista_alunos,'alunos'
                print s.id_municipio,s.cod_municipio,s.municipio,s.media_cn,s.media_ch,s.media_lc,s.media_mt,s.media_redacao,s.media_geral,s.total_alunos,s.total_escolas
                old = municipio_cod
                print '-----------------------------------'
