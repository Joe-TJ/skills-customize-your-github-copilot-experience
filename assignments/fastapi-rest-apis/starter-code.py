from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks = [
    Task(id=1, title="Read the FastAPI docs", completed=False),
    Task(id=2, title="Build the first endpoint", completed=True),
]


@app.get("/")
def read_root():
    return {"message": "TODO: add a welcome message"}


@app.get("/health")
def health_check():
    return {"status": "TODO"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")