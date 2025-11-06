from flask import Flask, request, jsonify

app = Flask(__name__)
tarefas = []
id_atual = 1

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global id_atual
    dados = request.json
    tarefa = {
        'id': id_atual,
        'titulo': dados.get('titulo'),
        'descricao': dados.get('descricao'),
        'prioridade': dados.get('prioridade'),
        'concluida': False
    }
    tarefas.append(tarefa)
    id_atual += 1
    return jsonify(tarefa), 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    prioridade = request.args.get('prioridade')
    if prioridade:
        filtradas = [t for t in tarefas if t['prioridade'] == prioridade]
        return jsonify(filtradas)
    return jsonify(tarefas)

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.json
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa.update({
                'titulo': dados.get('titulo', tarefa['titulo']),
                'descricao': dados.get('descricao', tarefa['descricao']),
                'prioridade': dados.get('prioridade', tarefa['prioridade']),
                'concluida': dados.get('concluida', tarefa['concluida'])
            })
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            return jsonify({'mensagem': 'Tarefa excluída'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
