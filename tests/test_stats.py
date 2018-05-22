import pytest
import sys
sys.path.append('/home/julian/so-exam3')

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'dar_cpu', return_value=1)
  response = client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8') == '{"CPU(%)": 1}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'dar_memoria', return_value=2)
  response = client.get('/v1/stats/memory')
  assert response.data.decode('utf-8') == '{"Memoria_Disponible": 2}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'dar_espacio', return_value=3)
  response = client.get('/v1/stats/disk')
  assert response.data.decode('utf-8') == '{"Espacio_Disco": 3}'
  assert response.status_code == 200

