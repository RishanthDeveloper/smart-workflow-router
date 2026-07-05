from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from router import WorkflowRouter

app = FastAPI(title="Smart Workflow Router API")
workflow_router = WorkflowRouter()

class TaskRequest(BaseModel):
    task_id: str
    description: str

class TaskResponse(BaseModel):
    task_id: str
    category: str
    status: str
    handler_response: dict

@app.post("/api/route", response_model=TaskResponse)
async def route_task_endpoint(task: TaskRequest):
    try:
        # Pass the task to the Smart Router
        result = await workflow_router.process_task(task.task_id, task.description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
