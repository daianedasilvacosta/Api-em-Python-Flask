from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask.helpers import send_from_directory
from dao import PedidoDao, UsuarioDao
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
app.config['MYSQL_DB'] = "requerimento"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = MySQL(app)
pedido_dao = PedidoDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = pedido_dao.listar()
    return render_template('lista.html', titulo='Pedidos', pedidos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Pedido')


@app.route('/criar', methods=['POST',])
def criar():
    nomepedido = request.form['nomepedido']
    categoriapedido = request.form['categoriapedido']
    descricaopedido = request.form['descricaopedido']
    precopedido = request.form['precopedido']
    pedido = Pedido(nomepedido, categoriapedido, descricaopedido, precopedido)
    pedido = pedido_dao.salvar(pedido)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{pedido.id}-{timestamp}.jpg')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    pedido = pedido_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Pedido',
                           pedido=pedido, capa_pedido=nome_imagem or 'capa_padrao.jpg')


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nomepedido = request.form['nomepedido']
    categoriapedido = request.form['categoriapedido']
    descricaopedido = request.form['descricaopedido']
    precopedido = request.form['precopedido']
    pedido = Pedido(nomepedido, categoriapedido, descricaopedido, precopedido, id=request.form['id'])

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(pedido.id)
    arquivo.save(f'{upload_path}/capa{pedido.id}-{timestamp}.jpg')
    pedido_dao.salvar(pedido)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    pedido_dao.deletar(id)
    flash('O pedido foi removido com sucesso!')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
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
