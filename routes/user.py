from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import user as schemas
from crud import user as user_crud

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """新しいユーザーを作成する"""
    return user_crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """指定されたIDのユーザーを取得する"""
    return user_crud.get_user(db, user_id)

@router.put("/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """指定されたIDのユーザーを更新する"""
    return user_crud.update_user(db, user_id, user)

# @router.delete("/{user_id}", response_model=schemas.UserResponse)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     """指定されたIDのユーザーを削除する"""
#     return user_crud.delete_user(db, user_id)

# @router.get("/", response_model=list[schemas.UserResponse])
# def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     """ユーザー一覧を取得する"""
#     users = db.query(models.User).offset(skip).limit(limit).all()
#     return users