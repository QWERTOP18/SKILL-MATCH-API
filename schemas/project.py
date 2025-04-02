from pydantic import BaseModel
from datetime import date

class ProjectBase(BaseModel):
    name: str
    memo: str | None = None
    document: str | None = None
    reference: str | None = None
    duration: date | None = None
    deadline: date | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True
