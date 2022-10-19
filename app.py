from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
     {
        'id':1,
        'name':'teste',
        'titulo': 'o senor dos aneis',
        'autor': 'bruno'
    },
    {
       'id':2,
        'name':'teste',
        'titulo': 'o senor dos aneis',
        'autor': 'bruno'  
    },
    {
         'id':3,
        'name':'teste',
        'titulo': 'o senor dos aneis',
        'autor': 'bruno'
    },
      {
         'id':4,
        'name':'teste',
        'titulo': 'o senor dos aneis',
        'autor': 'bruno'
    },
    {
         'id':5,
        'name':'teste',
        'titulo': 'o senor dos aneis',
        'autor': 'bruno'
    },

]



@app.route('/')
def index():
    return("vc esta na pagia index desta api!!!!!!")

    
@app.route('/livros')
def obter_livros():
    return jsonify(livros)



@app.route('/livros/<int:id>' ,methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)



@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indece].update(livro_alterado)
            return jsonify(livro[indece])




@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


def excluir_livro(id):
    for indece,livros in enumerate(livros):
      if livros.get('id') == id:
        del livros[indece]








app.run(port=5000,host='localhost',debug=True)





