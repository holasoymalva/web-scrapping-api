from flask import Flask, request, send_from_directory, jsonify, render_template, redirect
from flask_cors import CORS
import requests
# import
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/scripper',methods=['GET'])
def scripper():
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    print(results.prettify())

    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()
    return "scripper works"

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

