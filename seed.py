import csv
import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base, Question, Answer
from sqlalchemy.orm import sessionmaker

# データベースURLを設定
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# SQLAlchemyの設定
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベースセッションを作成
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def seed_questions(db: Session):
    # CSVファイルから質問を読み込み、データベースに挿入
    with open('seed/questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question_text = row['text']
            db_question = Question(text=question_text)
            db.add(db_question)
        db.commit()

def main():
    # データベースのテーブルを作成
    Base.metadata.create_all(bind=engine)

    # セッション開始
    db = next(get_db())

    try:
        # データのシーディング
        seed_questions(db)
        print("Questions have been seeded successfully.")
    except Exception as e:
        print(f"An error occurred while seeding the database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
    print("seed successed!")
