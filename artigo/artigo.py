from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask.helpers import send_from_directory
from dao import ProdutoDao, UsuarioDao
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
app.config['MYSQL_DB'] = "artigo"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = MySQL(app)
produto_dao = ProdutoDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = produto_dao.listar()
    return render_template('lista.html', titulo='Produtos', produtos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Produto')


@app.route('/criar', methods=['POST',])
def criar():
    nomeproduto = request.form['nomeproduto']
    descricaoproduto = request.form['descricaoproduto']
    precoproduto = request.form['precoproduto']
    produto = Produto(nomeproduto, descricaoproduto, precoproduto)
    produto = produto_dao.salvar(produto)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{produto.id}-{timestamp}.jpg')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    produto = produto_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Produto', produto=produto, capa_produto=nome_imagem or 'capa_padrao.jpg')


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nomeproduto = request.form['nomeproduto']
    descricaoproduto = request.form['descricaoproduto']
    precoproduto = request.form['precoproduto']
    produto = Produto(nomeproduto, descricaoproduto, precoproduto, id=request.form['id'])

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(produto.id)
    arquivo.save(f'{upload_path}/capa{produto.id}-{timestamp}.jpg')
    produto_dao.salvar(produto)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    produto_dao.deletar(id)
    flash('O porduto foi removido com sucesso!')
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
