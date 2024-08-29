from typing import Annotated
from fastapi import APIRouter, Depends

from db.repository import TaskRepository
from shemas import Task, TaskAdd, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("")
async def add_task(
    task: Annotated[TaskAdd, Depends()],
) -> TaskId:
    task_id =  await TaskRepository.add_task(task)
    return {"GOOD": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_tasks()
    return tasks