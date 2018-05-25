# so-exam3  

**Nombre:** Julián Niño  
**Curso:** Sistemas Operativos  
**Código:** A00328080  
**Correo:** juliannino01@hotmail.com  
**Correo Universitario:** julian.nino@correo.icesi.edu.co  

# Se debe implementar un servicio Web en flask con lo visto en clase 
- Cree un ambiente llamado julian  

-En este ambiente hay unas dependencias llamdas : requirements_dev.txt y requirements.txt, tambien 3 carpetas llamadas op_stats,
scripts y tests  

-En la carpeta llamada op_stats se encuentran dos archivos:  
# En stats.py se encuentra:  

import psutil

class Stats():

  @classmethod
  def dar_cpu(cls):
    percent = psutil.cpu_percent()
    return percent

  @classmethod
  def dar_memoria(cls):  
    ram_available = psutil.virtual_memory().available  
    return ram_available  

  @classmethod 
  def dar_espacio(cls):  
    free_disk = psutil.disk_usage('/').free  
    return free_disk  

# En app.py se encuentra:  


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
   
