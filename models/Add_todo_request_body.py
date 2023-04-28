from pydantic import BaseModel


class AddTodoRequestBody(BaseModel):
    """Base model for request body

    Args:
        BaseModel (_type_): inhetritade class
    """

    text: str
