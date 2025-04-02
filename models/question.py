from sqlalchemy import Column, Integer, String
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

    # スキル評価
    technical_skill = Column(Integer, default=0)
    problem_solving_ability = Column(Integer, default=0)
    communication_skill = Column(Integer, default=0)
    leadership_and_collaboration = Column(Integer, default=0)
    frontend_skill = Column(Integer, default=0)
    backend_skill = Column(Integer, default=0)
    infrastructure_skill = Column(Integer, default=0)
    security_awareness = Column(Integer, default=0)
