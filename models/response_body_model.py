from pydantic import BaseModel
from todo_model import TodoModel
from pagination_data_model import PaginationDataModel


class ResponseBodyModel(BaseModel):
    """Base model for the response body

    Args:
        BaseModel (BaseModel): inheritated class
    """
    todos: TodoModel | list[TodoModel]
    paginationData: PaginationDataModel