from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def details():
    location = input("Enter the location here: ")
    api_key = ""

    try:
        source = urllib.request.urlopen(''+api_key+'&q='+location)
        responseData = json.loads(source)
        data = {
            "latitute" : str(responseData['items'][0]['position']['lat']),
            "longitute" : str(responseData['items'][0]['position']['lon'])
        }

        return render_template('index.html', data=data, apikey=api_key)
    except (Exception):
        return render_template('index.html', error='Give the correct location')

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)