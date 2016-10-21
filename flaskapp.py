from flask import Flask, render_template
from get_chart import get_chart_list
from estado import define_map
from media import media_estado
from busca_aluno import make_page_aluno


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/algoritmos')
def alg():
    charts = get_chart_list()
    return render_template('algoritmos.html',charts = charts)

@app.route('/estados')
def est():
    return render_template('estados.html')

@app.route('/firebase')
def bases():
    return render_template('firebase.html')

@app.route('/map/<est>')
def map(est):
    info = define_map(est)
    if info[1] == 'ChIJq7dMA7UaRYkRTcp63_PsALY':
        parametros = []
    else:
        parametros = media_estado(est)
    return render_template('map.html',est=est,info=info,pam=parametros)

@app.route('/aluno/<num>')
def aluno(num):
    out =make_page_aluno(num)
    found = out[0]
    aluno = out[1]
    escola = out[2]
    pos_esc = out[3]
    graph_notas = out[4]
    return render_template('aluno.html',aluno=aluno,found=found,escola=escola,pos_esc=pos_esc,graph_notas=graph_notas)


if __name__ == '__main__':
    app.run()
