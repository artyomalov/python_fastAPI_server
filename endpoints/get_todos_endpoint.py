"""get todos endpoint

    Returns:
        JSON: list of todos and pagination data dict
    """
from database.session import db
from database.basemodel import Todo
from fastapi.responses import JSONResponse
from utils.calculate_pages_count import calculate_pages_count
from utils.get_find_arg import get_find_arg


async def get_todos(filterValue: str, pageNumber: int):
    """get todos endpoint

    Args:
        filterValue (str): value of the filter, got from the query srting
        pageNumber (int): value of the page number, got from the query string

    Returns:
        JSON: list of todos and pagination data dict    """
    try:
        find_arg = get_find_arg(filterValue)

        todos_count_data = calculate_pages_count(filter_value=filterValue,
                                                 page_number=pageNumber, data_base=db, model=Todo)

        some_todos_completed = todos_count_data['todos_total_count'] - \
            todos_count_data['active_todos_count'] > 0

        pagination_data = {
            'todos_total_count': todos_count_data['todos_total_count'],
            'active_todos_count': todos_count_data['active_todos_count'],
            'pages_count': todos_count_data['pages_count'],
            'some_todos_completed': some_todos_completed
        }

        if find_arg == None:
            todos_response = db.query(Todo).offset(
                todos_count_data['skip_counter']*5).limit(10).all()

            todos = [{'id': todo.id, 'text': todo.text,
                      'completed': todo.completed} for todo in todos_response]
            return JSONResponse({
                'todos': todos,
                'paginationData': pagination_data
            })

        todos_response = db.query(Todo).filter(Todo.completed == find_arg).offset(
            todos_count_data['skip_counter']*5).limit(10).all()

        todos = [{'id': todo.id, 'text': todo.text,
                  'completed': todo.completed} for todo in todos_response]
        return JSONResponse({
            'todos': todos,
            'paginationData': pagination_data
        })

    except Exception as err:
        return err
