from fastapi import FastAPI

from contextlib import asynccontextmanager

from db.database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Удаление БД...")
    
    await create_tables()
    print("Запуск БД...")
    yield
    print("Выключение БД...")

app = FastAPI(
    lifespan=lifespan
)
app.include_router(tasks_router)

