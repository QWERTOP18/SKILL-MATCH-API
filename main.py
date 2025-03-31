import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# 環境変数からデータベースURLを取得（デフォルトは SQLite）
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# SQLAlchemyの設定
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# データモデル
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    answers = relationship("Answer", back_populates="question")

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship("Question", back_populates="answers")

# FastAPIの設定
app = FastAPI()

# Pydanticモデル
class QuestionCreate(BaseModel):
    text: str

class AnswerCreate(BaseModel):
    text: str
    question_id: int

# データベースセッションを作成するユーティリティ関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# アプリ起動時にDBテーブルを作成
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# エンドポイント
@app.post("/questions")
async def create_question(question: QuestionCreate, db: SessionLocal = Depends(get_db)):
    db_question = Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.get("/questions")
async def read_questions(db: SessionLocal = Depends(get_db)):
    return db.query(Question).all()

@app.get("/questions/{question_id}")
async def read_question(question_id: int, db: SessionLocal = Depends(get_db)):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.post("/answers")
async def create_answer(answer: AnswerCreate, db: SessionLocal = Depends(get_db)):
    db_answer = Answer(text=answer.text, question_id=answer.question_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

@app.delete("/answers/{answer_id}")
async def delete_answer(answer_id: int, db: SessionLocal = Depends(get_db)):
    db_answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    db.delete(db_answer)
    db.commit()
    return {"detail": "Answer deleted"}

@app.get("/answers")
async def read_answers(db: SessionLocal = Depends(get_db)):
    return db.query(Answer).all()
