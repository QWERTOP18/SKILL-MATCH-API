from fastapi import FastAPI
from routes import user, project, task
from database import engine, Base

# DBテーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ルーターの登録
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(task.router, prefix="/questions", tags=["questions"])