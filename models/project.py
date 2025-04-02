from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    memo = Column(String)
    document = Column(String)
    reference = Column(String)
    duration = Column(Date, nullable=True)  # 期間（日付範囲が必要なら別の設計）
    deadline = Column(Date, nullable=True)

    users = relationship("User", back_populates="project")
    tasks = relationship("Task", back_populates="project")
