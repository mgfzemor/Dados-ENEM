import struct

def media_estado(estado):
    type_struct = struct.Struct('l h l 25s h 2s l h c h h h h h h f f f f h c')
    # And Imports ===========================================================

    var = 4

    uf = open('data/2014/estados/'+estado+'.bin','rb')
    i=0
    a=0
    media_math = 0 # Matematica e suas tecnologias:
    media_hum = 0 # Ciencias humanas e suas tecnologias:
    media_cod = 0 # Linguagens, codigos e suas tecnologias:
    media_natu = 0 # Ciencias da natureza e suas tecnologias:
    media_red = 0 # redacao
    media_geral = 0


    while True:
        bin_student = uf.read(type_struct.size)
        if bin_student == '':
            break
        student = type_struct.unpack(bin_student)
        if (student[11] == 0) or (student[12]==0) or (student[13]==0) or (student[14] == 0):
            a = a+1
        else:
            media_math = media_math + student[11]
            media_hum = media_hum + student[12]
            media_cod = media_cod + student[13]
            media_natu = media_natu + student[14]
            media_red = media_red + student[15]
            media_geral = media_geral + ((student[11]+student[12]+student[13]+student[14]+student[15])/5)
            i = i+1
    media_math = round(media_math/i,2)
    media_hum = round(media_hum/i,2)
    media_cod = round(media_cod/i,2)
    media_natu = round(media_natu/i,2)
    media_red = media_red/i
    media_geral = round(media_geral/i,2)


    print i,a
    return [i+a,media_math,media_hum,media_cod,media_natu, round(media_red,2),media_geral,i,a]

media_estado('SP')
