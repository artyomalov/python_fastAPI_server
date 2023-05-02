from pydantic import BaseModel
from todo_model import TodoModel


class AddTodoRequestBody(BaseModel):
    """Base model for request body

    Args:
        BaseModel (_type_): inhetritade class
    """

    text: str

