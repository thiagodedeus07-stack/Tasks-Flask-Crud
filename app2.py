from flask import Flask, request, jsonify
from models.tasks import Task

#(__name__) = "__main__" = executado de forma manual e nao importado d outro arquivo
app = Flask(__name__)

#CRUD = Create, Read, Update e Delete
#TAbela = Tarefa
#o Global é pra pegar o que ta fora da função

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("decription", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_task():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_taski(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completd = data['completed']
    return jsonify({"message": "Tarefa atualiazada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break
    
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})




if __name__ == "__main__":
    app.run(debug=True)