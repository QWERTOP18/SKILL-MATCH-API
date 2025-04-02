from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    memo: str | None = None
    project_id: int
    user_id: int | None = None
    status_id: int | None = None

    technical_skill: int = 0
    problem_solving_ability: int = 0
    communication_skill: int = 0
    leadership_and_collaboration: int = 0
    frontend_skill: int = 0
    backend_skill: int = 0
    infrastructure_skill: int = 0
    security_awareness: int = 0

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True
