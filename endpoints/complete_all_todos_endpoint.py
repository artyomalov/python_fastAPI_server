"""delete all completed todos endpoint

    Returns:
        JSON: deleted todo: {
        id: int
        text: str
        completed: bool
    },
    {
        'todosTotalCount': int
        'activeTodosCount': int
        'pagesCount': int
        'someTodosCompleted': bool
        'completed': bool
        }
    """

from fastapi.responses import JSONResponse
from database.session import db
from database.basemodel import Todo
from utils.calculate_pages_count import calculate_pages_count
from utils.get_find_arg import get_find_arg
from utils.get_todos import get_todos
from models.response_body_model import ResponseBodyModel

def complete_all_todos(filterValue: str) -> ResponseBodyModel:
    """delete all completed todos endpoint

    Args:
        filterValue (str): value of the filter that got from the query string

    Returns:
        JSON: todo, that has been deleted and pagination data:
            {
            'todosTotalCount': int
            'activeTodosCount': int
            'pagesCount': int
            'someTodosCompleted': bool
            'completed': bool
            }
    """
    try:
        find_arg = get_find_arg(filter_value=filterValue)


        result = db.query(Todo).filter(Todo.completed == False).update(
            {"completed": True}, synchronize_session='fetch')
        db.commit()
        completed = True

        
        if not result:
            result = db.query(Todo).filter(Todo.completed == True).update(
                {'completed': False}, synchronize_session='fetch')
            db.commit()
            completed = False


        todos_count_data = calculate_pages_count(
            filter_value=filterValue,
            page_number=1,
            data_base=db,
            model=Todo
        )
        some_todos_completed = todos_count_data['todos_total_count'] - \
            todos_count_data['active_todos_count'] > 0


        todos_response = get_todos(
            find_arg=find_arg,
            data_base=db,
            model=Todo,
            skip_counter=todos_count_data['skip_counter']
        )


        pagination_data = {
            'todosTotalCount': todos_count_data['todos_total_count'],
            'activeTodosCount': todos_count_data['active_todos_count'],
            'pagesCount': todos_count_data['pages_count'],
            'someTodosCompleted': some_todos_completed,
            'completed': completed
        }
        todos = [{
            '_id': todo.id,
            'text': todo.text,
            'completed': todo.completed
        } for todo in todos_response]


        return {
            'todos': todos,
            'paginationData': pagination_data
        }

    except Exception as err:
        return JSONResponse({'error': err}, status_code=500)
