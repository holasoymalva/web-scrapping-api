from flask import Flask, request, send_from_directory, jsonify, render_template, redirect
from flask_cors import CORS
import requests


app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test',methods=['GET'])
def hello_tets():
    jsonTest = {
        "codigoOperacion": 0,
        "datosSalida":"",
        "detalleMensaje": "El test Funciona de manera adecuada.",
        "mensaje": '',
        "tipoMensaje": "Operacion Exitosa",
    }
    return jsonTest


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, threaded=True)

