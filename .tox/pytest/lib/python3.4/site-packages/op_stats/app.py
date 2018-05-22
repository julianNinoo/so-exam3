from flask import Flask
import json
import sys
sys.path.append('/home/julian/so-exam3')
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def informacion_cpu():
    info_cpu = Stats.dar_cpu()
    return json.dumps({'CPU(%)': info_cpu})

@app.route('/v1/stats/memory')
def informacion_memoria():
    info_memoria = Stats.dar_memoria()
    return json.dumps({'Memoria_Disponible': info_memoria})

@app.route('/v1/stats/disk')
def informacion_disco():
    info_disco = Stats.dar_espacio()
    return json.dumps({'Espacio_Disco': info_disco})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
