import logging
from flask import Flask, jsonify, request, redirect, url_for
from waitress import serve
from model import BaseModel,Catalogo_Anuncio,create_table_anuncio,create_table_login,insert_many_anuncio,insert_many_login,login,select_many_anuncio

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/getget/lista/anuncio',methods=['GET'])
def listar_anuncio():
    return select_many_anuncio()

@app.route('/getget/cadastra/anuncio',methods=['POST'])
def inserir_many_anuncio():
    content = request.json
    return insert_many_anuncio(content)

if __name__ == '__main__':
    from waitress import serve
    app.run(host='0.0.0.0',port='8080',debug=False)
