from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # # スキル評価
    # technical_skill = Column(Integer, default=0)
    # problem_solving_ability = Column(Integer, default=0)
    # communication_skill = Column(Integer, default=0)
    # leadership_and_collaboration = Column(Integer, default=0)
    # frontend_skill = Column(Integer, default=0)
    # backend_skill = Column(Integer, default=0)
    # infrastructure_skill = Column(Integer, default=0)
    # security_awareness = Column(Integer, default=0)

    project = relationship("Project", back_populates="users")
    tasks = relationship("Task", back_populates="user")
