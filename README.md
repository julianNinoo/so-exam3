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


