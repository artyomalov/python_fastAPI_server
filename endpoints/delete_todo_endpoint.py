"""Delete todo endpoint

    Raises:
        Exception: _description_

    Returns:
        JSON: {
            pagesCount: int
            activeTodosCount: int
            todosTotalCount: int
        }
    """
from fastapi.responses import JSONResponse
from database.session import db
from database.basemodel import Todo
from utils.calculate_pages_count import calculate_pages_count
from exceptions.custom_exeption import CustomException


def delete_todo(id: int):
    """detete_todo_endpoint

    Args:
        id (int): Arg got from path params

    Raises:
        Exception: Exception

    Returns:
        JSON: {
            'pagesCount': int
            'activeTodosCount': int,
            'todosTotalCount': int
        }
    """
    try:
        deleted_todo = db.get(Todo, id)

        if not deleted_todo:
            raise CustomException('db error, no such todo', )
        db.delete(deleted_todo)
        db.commit()

        todos_count_data = calculate_pages_count(
            filter_value='all',
            page_number=1,
            data_base=db,
            model=Todo
        )

        return JSONResponse({
            'pagesCount': todos_count_data['pages_count'],
            'activeTodosCount': todos_count_data['active_todos_count'],
            'todosTotalCount': todos_count_data['todos_total_count']
        })

    except CustomException as err:
        error = err.db_error()
        return JSONResponse({'error': error['error']}, status_code=err['status_code'])
