from pydantic import BaseModel

class PaginationDataModel(BaseModel):
    todosTotalCount: int | None = None
    activeTodosCount: int 
    pagesCount: int | None = None
    someTodosCompleted: bool | None = None
    completed: bool | None = None