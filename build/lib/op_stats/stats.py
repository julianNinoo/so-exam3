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

