"""add todo endpoint

    Raises:
        Exception: _description_

    Returns:
        JSON: added todo and pagination data dict
    """

from fastapi.responses import JSONResponse
from database.session import db
from database.basemodel import Todo
from utils.calculate_pages_count import calculate_pages_count
from exceptions.custom_exeption import CustomException
from models.add_todo_model import AddTodoRequestBody


def add_todo(body: AddTodoRequestBody, filterValue: str, pageNumber: int):
    """_summary_

    Args:
        body (AddTodoRequestBody): request's body
        filterValue (str): filter value that got from  query string
        pageNumber (int): page number that got from  query string

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    try:
        todo_request = Todo(text=body.text, completed=False)

        db.add(todo_request)
        db.commit()
        db.refresh(todo_request)

        if not todo_request:
            raise CustomException('DB error')

        todos_count_data = calculate_pages_count(
            filter_value=filterValue,
            page_number=pageNumber,
            data_base=db,
            model=Todo)

        pagination_data = {
            'todosTotalCount': todos_count_data['todos_total_count'],
            'activeTodosCount': todos_count_data['active_todos_count'],
            'pagesCount': todos_count_data['pages_count'],
        }
        new_todo = {
            '_id': todo_request.id,
            'text': todo_request.text,
            'completed': todo_request.completed,
        }

        return JSONResponse(
            {
                'todos': new_todo,
                'paginationData': pagination_data
            }
        )

    except CustomException as err:
        return err

    except Exception as err:
        return err
