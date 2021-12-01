from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask.helpers import send_from_directory
from dao import ClienteDao, FuncionarioDao
from flask_mysqldb import MySQL
from models import *
import os
import time

app = Flask(__name__)
import os

app.secret_key = 'alura'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "shopping"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = MySQL(app)
cliente_dao = ClienteDao(db)
funcionario_dao = FuncionarioDao(db)

@app.route('/')
def index():
    lista = cliente_dao.listar()
    return render_template('lista.html', titulo='Clientes',
                           clientes=lista)


@app.route('/novo')
def novo():
    if 'funcionario_logado' not in session or session['funcionario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Cliente')


@app.route('/criar', methods=['POST',])
def criar():
    nomecliente = request.form['nomecliente']
    cpfcliente = request.form['cpfcliente']
    enderecocliente = request.form['enderecocliente']
    emailcliente = request.form['emailcliente']
    cliente = Cliente(nomecliente, cpfcliente, enderecocliente, emailcliente)
    cliente = cliente_dao.salvar(cliente)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{cliente.id}-{timestamp}.jpg')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'funcionario_logado' not in session or session['funcionario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    cliente = cliente_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Cliente', cliente=cliente,
                           capa_cliente=nome_imagem or 'capa_padrao.jpg')


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nomecliente = request.form['nomecliente']
    cpfcliente = request.form['cpfcliente']
    enderecocliente = request.form['enderecocliente']
    emailcliente = request.form['emailcliente']
    cliente = Cliente(nomecliente, cpfcliente, enderecocliente, emailcliente, id=request.form['id'])

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(cliente.id)
    arquivo.save(f'{upload_path}/capa{cliente.id}-{timestamp}.jpg')
    cliente_dao.salvar(cliente)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    cliente_dao.deletar(id)
    flash('O cliente foi removido com sucesso!')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    funcionario = funcionario_dao.buscar_por_id(request.form['funcionario'])
    if funcionario:
        if funcionario.senha == request.form['senha']:
            session['funcionario_logado'] = funcionario.id
            flash(funcionario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['funcionario_logado'] = None
    flash('Nenhum funcionário logado!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo))


app.run(debug=True)
