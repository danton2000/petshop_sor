from flask import Flask, render_template

app = Flask(__name__)

produtos_list = [
    {
        'nome': 'Ração',
        'url_link': 'racao',
        'descricao': 'Comida para cães',
        'destaque': 1
    },
    {
        'nome': 'Coleiras',
        'url_link': 'coleira',
        'descricao': 'Coleira para cães',
        'destaque': 1
    },
    {
        'nome': 'Roupas',
        'url_link': 'roupas',
        'descricao': 'Roupa para cães',
        'destaque': 1
    },
    {
        'nome': 'Brinquedos',
        'url_link': 'brinquedos',
        'descricao': 'Brinquedos para cães'
        
    },
    {
        'nome': 'Cama',
        'url_link': 'cama',
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
        print(produto)
        if produto_nome == produto['url_link']:
            
            return render_template(
                "produto_detalhes.html",
                nome=produto['nome'],
                produto=produto
            )   
    

@app.route("/servicos/")
def servicos():
    return render_template("servicos.html", servicos=servicos_list)