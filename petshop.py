from flask import Flask, render_template, request, redirect, url_for
# request todo conteudo que o usuário enviou para a gente
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():

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

#preparando a rota para receber as requisões do tipo get e post
@app.route('/servicos/servico-cadastro', methods=('GET', 'POST'))
def servicos_cadastro():

    #quer enviar algo junto
    if request.method == 'POST':

        nome = request.form['txt_nome']

        url_link = request.form['txt_url_link']

        descricao = request.form['txt_descricao']

        preco = request.form['txt_preco']

        destaque = 0

        if 'cbx_destaque' in request.form:
            destaque = 1

        con = sqlite3.connect('petshop.db')

        cur = con.cursor()

        cur.execute(f"INSERT INTO servicos ( nome, url_link, descricao, preco, destaque ) VALUES ('{nome}', '{url_link}', '{descricao}', '{preco}', {destaque})")

        con.commit()

        con.close

        #redirecionando o cliente para a rota de servicos

        return redirect(url_for('servicos'))


    return render_template('servico-cadastro.html')

@app.route('/produtos/produto-cadastro', methods=('GET', 'POST'))
def produto_cadastro():

    #quer enviar algo junto
    if request.method == 'POST':

        nome = request.form['txt_nome']

        url_link = request.form['txt_url_link']

        descricao = request.form['txt_descricao']

        preco = request.form['txt_preco']

        destaque = 0

        if 'cbx_destaque' in request.form:
            destaque = 1

        con = sqlite3.connect('petshop.db')

        cur = con.cursor()

        cur.execute(f"INSERT INTO produtos ( nome, url_link, descricao, preco, destaque ) VALUES ('{nome}', '{url_link}', '{descricao}', '{preco}', {destaque})")

        con.commit()

        con.close

        #redirecionando o cliente para a rota de servicos

        return redirect(url_for('servicos'))

    return render_template('produto-cadastro.html')     