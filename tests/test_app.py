import pytest
from src.app import app

@pytest.fixture
def cliente():
    app.testing = True
    return app.test_client()

def test_criar_tarefa(cliente):
    resposta = cliente.post('/tarefas', json={
        'titulo': 'Estudar Engenharia de Software',
        'descricao': 'Ler capítulo 3',
        'prioridade': 'Alta'
    })
    assert resposta.status_code == 201
    assert resposta.json['titulo'] == 'Estudar Engenharia de Software'
