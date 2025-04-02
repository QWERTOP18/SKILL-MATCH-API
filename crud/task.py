from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.task import Task
from models.user import User
from models.project import Project
# from models.status import Status
from typing import Optional, Dict, Any

# タスク作成
def create_task(db: Session, task_data: Dict[str, Any]) -> Task:
    # 関連エンティティの存在確認
    if "user_id" in task_data and task_data["user_id"]:
        user = db.query(User).filter(User.id == task_data["user_id"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

    if "project_id" in task_data and task_data["project_id"]:
        project = db.query(Project).filter(Project.id == task_data["project_id"]).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

    # if "status_id" in task_data and task_data["status_id"]:
    #     status = db.query(Status).filter(Status.id == task_data["status_id"]).first()
    #     if not status:
    #         raise HTTPException(status_code=404, detail="Status not found")

    # タスク作成
    task = Task(**task_data)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# タスク取得
def get_task(db: Session, task_id: int) -> Task:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# タスク一覧取得
def get_tasks(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    project_id: Optional[int] = None
    # status_id: Optional[int] = None
) -> list[Task]:
    query = db.query(Task)
    
    # フィルタリング
    if user_id:
        query = query.filter(Task.user_id == user_id)
    if project_id:
        query = query.filter(Task.project_id == project_id)
    # if status_id:
    #     query = query.filter(Task.status_id == status_id)
        
    return query.offset(skip).limit(limit).all()

# タスク更新
def update_task(db: Session, task_id: int, task_data: Dict[str, Any]) -> Task:
    task = get_task(db, task_id)
    
    # 関連エンティティの存在確認
    if "user_id" in task_data and task_data["user_id"]:
        user = db.query(User).filter(User.id == task_data["user_id"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

    if "project_id" in task_data and task_data["project_id"]:
        project = db.query(Project).filter(Project.id == task_data["project_id"]).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

    # if "status_id" in task_data and task_data["status_id"]:
    #     status = db.query(Status).filter(Status.id == task_data["status_id"]).first()
    #     if not status:
    #         raise HTTPException(status_code=404, detail="Status not found")
    
    # 更新するフィールドを設定
    for key, value in task_data.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

# タスク削除
def delete_task(db: Session, task_id: int) -> Task:
    task = get_task(db, task_id)
    db.delete(task)
    db.commit()
    return task