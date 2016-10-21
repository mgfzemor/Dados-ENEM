from random import randint
def get_chart_list():
    list_n = open('static/chart/data/chart_list_n.txt','r')
    list_c = open('static/chart/data/chart_list_c.txt','r')

    chart_n = list_n.readlines()
    chart_c = list_c.readlines()
    saida_n = []
    saida_c = []
    color = []
    for lin in chart_n:
        new_line =  lin.split(',',1)
        new_line[1] = new_line[1].replace("\n","")
        new_line[1] = new_line[1].replace("[","")
        new_line[1] = new_line[1].replace("]","")
        cor = randint(0,255)
        cor1 = randint(0,255)
        cor2 = randint(0,255)
        cores = []
        cores.append(cor)
        cores.append(cor1)
        cores.append(cor2)
        new_line.append(cores)
        saida_n.append(new_line)



    for lin in chart_c:
        new_line =  lin.split(',',1)
        new_line[1] = new_line[1].replace("\n","")
        new_line[1] = new_line[1].replace("[","")
        new_line[1] = new_line[1].replace("]","")
        cor = randint(0,255)
        cor1 = randint(0,255)
        cor2 = randint(0,255)
        cores = []
        cores.append(cor)
        cores.append(cor1)
        cores.append(cor2)
        new_line.append(cores)
        saida_c.append(new_line)

    return [saida_n,saida_c]
