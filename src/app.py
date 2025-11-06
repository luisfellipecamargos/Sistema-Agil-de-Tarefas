from flask import Flask, request, jsonify, render_template, redirect
import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    global tarefas, id_atual
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as f:
            try:
                tarefas = json.load(f)
                if tarefas:
                    id_atual = max(t["id"] for t in tarefas) + 1
                else:
                    id_atual = 1
            except json.JSONDecodeError:
                tarefas = []
                id_atual = 1
    else:
        tarefas = []
        id_atual = 1

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)

app = Flask(__name__)
carregar_tarefas()

@app.route("/")
def pagina_inicial():
    return render_template("index.html", tarefas=tarefas)

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    prioridade = request.args.get("prioridade")
    if prioridade:
        filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
        return jsonify(filtradas)
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    global id_atual
    dados = request.form if request.form else request.get_json()
    tarefa = {
        "id": id_atual,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "prioridade": dados["prioridade"]
    }
    tarefas.append(tarefa)
    id_atual += 1
    salvar_tarefas()
    return redirect("/")

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa.update(dados)
            salvar_tarefas()
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            salvar_tarefas()
            return jsonify({"mensagem": "Tarefa excluída"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
