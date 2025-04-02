from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str
    memo: Optional[str] = None
    project_id: int
    user_id: Optional[int] = None
    # color: str = "#FF5733"
    # status:str = "未着手"
    # status_id: Optional[int] = None

    # スキル評価フィールド
    technical_skill: int = Field(default=0, ge=0, le=5, description="技術スキルの評価 (0-5)")
    problem_solving_ability: int = Field(default=0, ge=0, le=5, description="問題解決能力の評価 (0-5)")
    communication_skill: int = Field(default=0, ge=0, le=5, description="コミュニケーションスキルの評価 (0-5)")
    leadership_and_collaboration: int = Field(default=0, ge=0, le=5, description="リーダーシップと協働性の評価 (0-5)")
    frontend_skill: int = Field(default=0, ge=0, le=5, description="フロントエンドスキルの評価 (0-5)")
    backend_skill: int = Field(default=0, ge=0, le=5, description="バックエンドスキルの評価 (0-5)")
    infrastructure_skill: int = Field(default=0, ge=0, le=5, description="インフラストラクチャスキルの評価 (0-5)")
    security_awareness: int = Field(default=0, ge=0, le=5, description="セキュリティ意識の評価 (0-5)")

class TaskCreate(TaskBase):
    """タスク作成用スキーマ"""
    pass

class TaskUpdate(BaseModel):
    """タスク更新用スキーマ - すべてのフィールドはオプション"""
    title: Optional[str] = None
    memo: Optional[str] = None
    project_id: Optional[int] = None
    user_id: Optional[int] = None
    # color: Optional[str] = None
    # status: Optional[str] = None
    # status_id: Optional[int] = None

    technical_skill: Optional[int] = Field(None, ge=0, le=5)
    problem_solving_ability: Optional[int] = Field(None, ge=0, le=5)
    communication_skill: Optional[int] = Field(None, ge=0, le=5)
    leadership_and_collaboration: Optional[int] = Field(None, ge=0, le=5)
    frontend_skill: Optional[int] = Field(None, ge=0, le=5)
    backend_skill: Optional[int] = Field(None, ge=0, le=5)
    infrastructure_skill: Optional[int] = Field(None, ge=0, le=5)
    security_awareness: Optional[int] = Field(None, ge=0, le=5)

class TaskResponse(TaskBase):
    """タスクレスポンス用スキーマ"""
    id: int

    class Config:
        orm_mode = True
        # Pydantic v2からは以下の書き方に変更されています
        # model_config = {"from_attributes": True}