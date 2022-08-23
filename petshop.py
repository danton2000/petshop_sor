from flask import Flask, render_template

import sqlite3

app = Flask(__name__)

@app.route("/")
def index():

    servicos_destaques = []

    con = sqlite3.connect('petshop.db')

    cur = con.cursor()

    cur.execute("SELECT nome, url_link FROM produtos WHERE destaque = 1 ORDER BY nome")

    destaque_produtos_bd = cur.fetchall()

    cur.execute("SELECT nome, url_link FROM servicos WHERE destaque = 1 ORDER BY nome")

    destaque_servicos_bd = cur.fetchall()

    con.close()

    return render_template("index.html", produtos=destaque_produtos_bd, servicos=destaque_servicos_bd)

@app.route("/produtos/")
def produtos():

    con = sqlite3.connect("petshop.db")

    cur = con.cursor()

    cur.execute("SELECT nome, url_link FROM produtos")

    #lista
    produtos_bd = cur.fetchall()

    con.close()    

    return render_template("produtos.html", produtos=produtos_bd)

@app.route("/produtos/<produto_nome>/detalhes")
def produtos_detalhes(produto_nome):

    con = sqlite3.connect("petshop.db")

    cur = con.cursor()

    cur.execute(
        "SELECT nome, descricao, preco FROM produtos WHERE url_link = ?",
        (produto_nome,))

    # (,) tupla de 1 tem requer uma virgual

    #lista, retorna só 1 tupla
    produto_bd = cur.fetchone()

    con.close()   

    return render_template(
        "produto_detalhes.html",
        produto=produto_bd
    )       
    

@app.route("/servicos/")
def servicos():

    con = sqlite3.connect("petshop.db")

    cur = con.cursor()

    cur.execute("SELECT nome, url_link FROM servicos")

    #lista
    servicos_bd = cur.fetchall()

    con.close()    

    return render_template("servicos.html", servicos=servicos_bd)

@app.route("/servicos/<servico_nome>/detalhes")
def servicos_detalhes(servico_nome):

    con = sqlite3.connect("petshop.db")

    cur = con.cursor()

    cur.execute(
        "SELECT nome, descricao, preco FROM servicos WHERE url_link = ?",
        (servico_nome,))

    # (,) tupla de 1 tem requer uma virgual

    #lista, retorna só 1 tupla
    servico_bd = cur.fetchone()

    con.close()   

    return render_template(
        "servico_detalhes.html",
        servico=servico_bd
    )       