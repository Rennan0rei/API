from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

usuarios = [
    'Jade Picon',
    'Pedro Pedroso',
    'Robnilson O grande',
    'Claudenilson oproprio',
    'Ana Maria Braga',
    'Icaro Ferdinando'
]
 
@app.route('/users', methods=['GET'])
def pegar_usuarios():
    return jsonify({'users': usuarios})


@app.route('/user/<numero>', methods=['GET'])
def pegar_usuario(numero):
    localNumber = int(numero)
 
    return jsonify({'users': usuarios[localNumber]})

@app.route('/user/novo', methods = ['POST'])
def criar_novo_usuario():
    novo_usuario = request.json
    print (novo_usuario)
    return jsonify({
        'user': novo_usuario,
        'message': 'Usuario criado com sucesso!'
    })
 
if __name__ == '__main__':
    app.run(port=3000)