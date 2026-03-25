from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    created_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)

