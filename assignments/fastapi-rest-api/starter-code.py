from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = {}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Tarefas!"}

@app.get("/tasks")
def list_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tasks[task_id]

@app.post("/tasks")
def create_task(task: dict):
    task_id = len(tasks) + 1
    task["id"] = task_id
    tasks[task_id] = task
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    task["id"] = task_id
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tasks[task_id]
    return {"ok": True}
