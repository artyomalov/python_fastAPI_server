from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    text: str
    completed: bool
