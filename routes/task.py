from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from crud import task as task_crud

router = APIRouter()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """新しいタスクを作成する"""
    return task_crud.create_task(db, task_data.dict())

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None,
    project_id: Optional[int] = None,
    status_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """タスク一覧を取得する（オプションのフィルタあり）"""
    tasks = task_crud.get_tasks(
        db, 
        skip=skip, 
        limit=limit, 
        user_id=user_id, 
        project_id=project_id,
        status_id=status_id
    )
    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """指定されたIDのタスクを取得する"""
    return task_crud.get_task(db, task_id)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    """指定されたIDのタスクを更新する"""
    return task_crud.update_task(db, task_id, task_data.dict(exclude_unset=True))

@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """指定されたIDのタスクを削除する"""
    return task_crud.delete_task(db, task_id)