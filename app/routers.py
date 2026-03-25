from fastapi import APIRouter
from .schemas.post_schemas import PostRead
from .models.post_model import Post

router = APIRouter(prefix="/post", tags=["post"])

@router.get("/", response_model=PostRead)
def get_all_posts():
    return PostRead(posts=[Post(post="ok")])
