from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

def getrate(fr, to):
    url = f"https://www.x-rates.com/calculator/?from={fr}&to={to}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()[:-4]
    rate = float(rate)
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency API</h1><br><h2>goto /api/v1/usd-eur</h2>'

@app.route('/api/v1/<incur>-<outcur>')
def apiv1(incur,outcur):
    rate = getrate(incur,outcur)
    result = {
        'input_currency' : incur,
        'output_currency' : outcur,
        'rate' : rate
    }
    return jsonify(result)

app.run(host='0.0.0.0')