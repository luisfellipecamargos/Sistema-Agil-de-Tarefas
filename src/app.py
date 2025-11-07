from flask import Flask, request, jsonify, render_template, redirect
import json
import os

app = Flask(__name__)
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "tarefas.json")

def carregar_tarefas():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

tarefas = carregar_tarefas()

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.form if request.form else request.get_json()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "prioridade": dados["prioridade"],
        "status": dados.get("status", "pendente")
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return redirect("/") if request.form else jsonify(nova_tarefa)

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa.update(dados)
            salvar_tarefas(tarefas)
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id]
    salvar_tarefas(tarefas)
    return jsonify({"mensagem": "Tarefa excluída"})
