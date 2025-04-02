from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    """ユーザーの基本情報を定義するベースモデル"""
    username: str = Field(..., min_length=3, max_length=50, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")

class UserCreate(UserBase):
    """ユーザー作成時に使用するモデル"""
    password: str = Field(..., min_length=8, description="パスワード（8文字以上）")

class UserUpdate(BaseModel):
    """ユーザー情報更新時に使用するモデル（すべてのフィールドはオプション）"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    """APIレスポンスとして返すユーザー情報モデル"""
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True
        # Pydantic v2の場合は以下を使用
        # model_config = {"from_attributes": True}

class UserInDB(UserResponse):
    """データベース内のユーザー情報を表すモデル（内部使用）"""
    hashed_password: str