from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str

    technical_skill: int = 0
    problem_solving_ability: int = 0
    communication_skill: int = 0
    leadership_and_collaboration: int = 0
    frontend_skill: int = 0
    backend_skill: int = 0
    infrastructure_skill: int = 0
    security_awareness: int = 0

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int

    class Config:
        orm_mode = True
