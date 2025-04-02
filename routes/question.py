from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_questions():
    return {"message": "List of questions"}

@router.post("/")
async def create_question(question: str):
    return {"message": f"Question '{question}' created"}

@router.get("/{question_id}")
async def get_question(question_id: int):
    return {"message": f"Details of question with id {question_id}"}
