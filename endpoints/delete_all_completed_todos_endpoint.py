"""delete all todos endpoint

    Raises:
        Exception: server error

    Returns:
       JSON: list of todos and pagination data
    """

from fastapi.responses import JSONResponse
from database.session import db
from database.basemodel import Todo
from utils.get_todos_servise import get_todos_handler
from exceptions.custom_exeption import CustomException
from utils.calculate_pages_count_servise import calculate_pages_count
from utils.get_find_arg_servise import get_find_arg


def delete_all_completed_todos(filterValue: str):
    """delete all todos endpoint

    Args:
        filterValue (str): value of the filter that got from the query string
    Raises:
        Exception: server error

    Returns:
        JSON: list of todos and pagination data
    """

    try:
        result = db.query(Todo).filter(Todo.completed == True).delete(
            synchronize_session='fetch')
        db.commit()
        if not result:
            raise CustomException('DB error')

        find_arg = get_find_arg(filter_value=filterValue)

        todos_count_data = calculate_pages_count(
            filter_value=filterValue,
            page_number=1,
            data_base=db,
            model=Todo
        )

        some_todos_completed = todos_count_data['todos_total_count'] - \
            todos_count_data['active_todos_count'] > 0

        pagination_data = {
            'todosTotalCount': todos_count_data['todos_total_count'],
            'activeTodosCount': todos_count_data['active_todos_count'],
            'pagesCount': todos_count_data['pages_count'],
            'someTodosCompleted': some_todos_completed
        }

        todos_response = get_todos_handler(
            find_arg=find_arg,
            data_base=db,
            model=Todo,
            skip_counter=todos_count_data['skip_counter']
        )

        todos = [{
            '_id': todo.id,
            'text': todo.text,
            'completed': todo.completed
        } for todo in todos_response]

        return {
            'todos': todos,
            'paginationData': pagination_data
        }
    except CustomException as err:
        return err
    except Exception as err:
        return JSONResponse({'error': err}, status_code=500)
