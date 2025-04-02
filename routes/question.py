from fastapi import APIRouter

router = APIRouter()

# Example of a GET endpoint to retrieve all questions
@router.get("/")
async def get_questions():
    return {"message": "List of questions"}

# Example of a POST endpoint to create a new question
@router.post("/")
async def create_question(question: str):
    return {"message": f"Question '{question}' created"}

# Example of a GET endpoint to retrieve a specific question by id
@router.get("/{question_id}")
async def get_question(question_id: int):
    return {"message": f"Details of question with id {question_id}"}
