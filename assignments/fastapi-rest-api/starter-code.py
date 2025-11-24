"""
FastAPI Task Management API - Starter Code

This is a starter template for building a REST API with FastAPI.
Complete the TODO sections to implement a full CRUD API for managing tasks.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# Pydantic model for Task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory database (list of tasks)
tasks_db: List[Task] = [
    Task(id=1, title="Learn FastAPI", description="Study FastAPI documentation", completed=False),
    Task(id=2, title="Build an API", description="Create a REST API project", completed=False)
]

# TODO: Implement GET endpoint to retrieve all tasks
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API. Visit /docs for API documentation."}

# TODO: Implement GET endpoint to retrieve all tasks
# Hint: Use @app.get("/tasks") and return tasks_db

# TODO: Implement GET endpoint to retrieve a single task by ID
# Hint: Use @app.get("/tasks/{task_id}") and raise HTTPException if not found

# TODO: Implement POST endpoint to create a new task
# Hint: Use @app.post("/tasks", status_code=201) and append to tasks_db

# TODO: Implement PUT endpoint to update an existing task
# Hint: Use @app.put("/tasks/{task_id}") and update the task in tasks_db

# TODO: Implement DELETE endpoint to remove a task
# Hint: Use @app.delete("/tasks/{task_id}", status_code=204) and remove from tasks_db

# Run the application
# To start the server, run: uvicorn starter-code:app --reload
