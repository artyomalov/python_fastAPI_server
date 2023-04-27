from fastapi import Body
from fastapi.responses import JSONResponse
from database.basemodel import Todo
from database.session import db


# class DeleteTodoRequestBody(BaseModel):
#     """Base model for request body

#     Args:
#         BaseModel (_type_): _description_
#     """
#     prop: str
#     value: bool


def update_todo(id: int, pageNumber: int, filterValue: str, body=Body()):
    """update edpoint for todo API

    Args:
        id (int): todo's id that got from path
        page_number (int): page number that got from  query string
        filterValue (str): filter value that got from  query string
        body (DeleteTodoRequestBody): request body
    Returns:
        JSON: data
    """
    try:
        updating_todo_prop = body['prop']
        updating_todo_value = not body['value'] if body['prop'] == 'completed' else body['value']
        returned_todo_query = db.get(Todo, id)
        setattr(returned_todo_query, updating_todo_prop, updating_todo_value)
        db.commit()

        returned_todo = {
            'id': returned_todo_query.id,
            'text': returned_todo_query.text,
            'completed': returned_todo_query.completed
        }
        print(returned_todo)
        active_todos_count = db.query(Todo).filter(
            Todo.completed is False).count()
        pagination_data = {
            'activeTodosCount': active_todos_count
        }

        return JSONResponse({'returnedTodo': returned_todo, 'pagination_data': pagination_data})
    except Exception as err:
        return JSONResponse({'error': err}, status_code=500)
