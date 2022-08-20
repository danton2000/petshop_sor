from flask import Flask, render_template

app = Flask(__name__)

produtos_list = [
    {
        'nome': 'Ração',
        'descricao': 'Comida para cães',
        'destaque': 1
    },
    {
        'nome': 'Coleira',
        'descricao': 'Coleira para cães',
        'destaque': 1
    },
    {
        'nome': 'Roupa',
        'descricao': 'Roupa para cães',
        'destaque': 1
    },
    {
        'nome': 'Brinquedos',
        'descricao': 'Brinquedos para cães'
        
    },
    {
        'nome': 'Cama',
        'descricao': 'Cama para cães'
    }
]

servicos_list = [
    {
        'nome': 'Banho',
        'destaque': 1
    },
    {
        'nome': 'Ducha e Corte na régua',
        'destaque': 1
    },
    {
        'nome': 'Creche'
    }
]

@app.route("/")
def index():

    produtos_destaques = []

    for produto in produtos_list:

        if 'destaque' in produto:

            produtos_destaques.append(produto)

    servicos_destaques = []

    for servico in servicos_list:

        if 'destaque' in servico:

            servicos_destaques.append(servico)

    return render_template("index.html", produtos=produtos_destaques, servicos=servicos_destaques)

@app.route("/produtos/")
def produtos():
    return render_template("produtos.html", produtos=produtos_list)

@app.route("/produtos/<produto_nome>/detalhes")
def produtos_detalhes(produto_nome):

    for produto in produtos_list:

        if produto_nome == produto['nome']:

            return render_template(
                "produto_detalhes.html",
                nome=produto_nome,
                produto=produto
            )
        return render_template("produto_detalhes.html", nome=produto_nome)     
    

@app.route("/servicos/")
def servicos():
    return render_template("servicos.html", servicos=servicos_list)