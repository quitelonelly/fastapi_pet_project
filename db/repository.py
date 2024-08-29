from sqlalchemy import select
from db.database import TaskORM, new_session
from shemas import Task, TaskAdd

class TaskRepository:
    @classmethod
    async def add_task(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()

            # Convert TaskORM instances to dictionaries
            task_dicts = [task_model_to_dict(task_model) for task_model in task_models]

            # Validate and create Task instances
            task_schemas = [Task(**task_dict) for task_dict in task_dicts]
            return task_schemas

def task_model_to_dict(task_model: TaskORM) -> dict:
    # Assuming TaskORM has attributes `id`, `name`, and `description`
    return {
        'id': task_model.id,
        'name': task_model.name,
        'description': task_model.description
    }
