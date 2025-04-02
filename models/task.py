from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    memo = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))

    # スキル評価
    technical_skill = Column(Integer, default=0)
    problem_solving_ability = Column(Integer, default=0)
    communication_skill = Column(Integer, default=0)
    leadership_and_collaboration = Column(Integer, default=0)
    frontend_skill = Column(Integer, default=0)
    backend_skill = Column(Integer, default=0)
    infrastructure_skill = Column(Integer, default=0)
    security_awareness = Column(Integer, default=0)

    project = relationship("Project", back_populates="tasks")
    user = relationship("User", back_populates="tasks")
