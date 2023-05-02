"""update edpoint for todo API
    Returns:
    JSON: list of todos and pagination data
"""
from fastapi import Body
from fastapi.responses import JSONResponse
from database.basemodel import Todo
from database.session import db


def update_todo(id: int, body=Body()):
    """update edpoint for todo API

    Args:
        id (int): todo's id that got from path
        page_number (int): page number that got from  query string
        filterValue (str): filter value that got from  query string
        body (DeleteTodoRequestBody): request body
    Returns:
        JSON: list of todos and pagination data
    """
    try:
        updating_todo_prop = body['prop']
        updating_todo_value = not body['value'] if body['prop'] == 'completed' \
            else body['value']
        returned_todo_query = db.get(Todo, id)

        setattr(
            returned_todo_query,
            updating_todo_prop,
            updating_todo_value
        )
        db.commit()

        returned_todo = {
            '_id': returned_todo_query.id,
            'text': returned_todo_query.text,
            'completed': returned_todo_query.completed
        }

        active_todos_count = db.query(Todo).filter(
            Todo.completed == False).count()
        pagination_data = {
            'activeTodosCount': active_todos_count
        }
        return JSONResponse({
            'todos': returned_todo,
            'paginationData': pagination_data
        })
    except Exception as err:
        return JSONResponse({'error': err}, status_code=500)
