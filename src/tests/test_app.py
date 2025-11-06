import pytest
from app import app, tarefas

@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente

def test_listar_tarefas(cliente):
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)

def test_criar_tarefa(cliente):
    nova = {
        "titulo": "Teste",
        "descricao": "Tarefa de teste",
        "prioridade": "Alta"
    }
    resposta = cliente.post("/tarefas", json=nova)
    assert resposta.status_code in [200, 302]
    assert any(t["titulo"] == "Teste" for t in tarefas)
