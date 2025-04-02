from fastapi import APIRouter

router = APIRouter()


# questionsはDatabaseを使わないので、CRUD処理は不要　csvからデータを取得して返すだけにする
@router.get("/")
async def get_questions():
    return {"message": "List of questions"}

