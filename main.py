from flask import *
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get("http://192.168.1.110:5000/states")
    res_json = json.loads(r.text)
    modules = res_json['modules']
    #remplissages = res_json['remplissages']
    remplissages = {}
    return render_template('index.html', modules=modules, remplissages=remplissages)

app.run(host="0.0.0.0", port=5000)
