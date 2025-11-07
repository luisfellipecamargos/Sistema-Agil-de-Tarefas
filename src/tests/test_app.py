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

def test_criar_tarefa_com_status(cliente):
    nova = {
        "titulo": "Teste com status",
        "descricao": "Tarefa de teste",
        "prioridade": "Alta",
        "status": "concluída"
    }
    resposta = cliente.post("/tarefas", json=nova)
    assert resposta.status_code in [200, 302]
    assert any(t["titulo"] == "Teste com status" and t["status"] == "concluída" for t in tarefas)
