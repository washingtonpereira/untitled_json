from dados import dados5
from api_language import Livros

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def helo():
    return 'Bem vindo'

@app.route('/api')
def api():
    return jsonify(dados5)


if __name__ == '__main__':
    app.run(debug = True)