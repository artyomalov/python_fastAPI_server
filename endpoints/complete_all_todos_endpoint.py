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


def complete_all_todos(filterValue: str):
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
        result = db.query(Todo).filter(Todo.completed == False).update(
            {"completed": True}, synchronize_session='fetch')
        db.commit()

        find_arg = get_find_arg(filter_value=filterValue)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>", find_arg)
        if not result:
            result = db.query(Todo).filter(Todo.completed == True).update(
                {'completed': False}, synchronize_session='fetch')

            todos_count_data = calculate_pages_count(
                filter_value=filterValue, page_number=1, data_base=db, model=Todo)

            some_todos_completed = todos_count_data['todos_total_count'] - \
                todos_count_data['active_todos_count'] > 0

            pagination_data = {
                'todosTotalCount': todos_count_data['todos_total_count'],
                'activeTodosCount': todos_count_data['active_todos_count'],
                'pagesCount': todos_count_data['pages_count'],
                'someTodosCompleted': some_todos_completed,
                'completed': False
            }

            todos_response = db.query(Todo).order_by(Todo.id.desc()).\
                filter(Todo.completed == find_arg).offset(todos_count_data['skip_counter']*5).limit(10).all()\
                if find_arg != None\
                else db.query(Todo).offset(todos_count_data['skip_counter']*5).limit(10).all()

            todos = [{
                '_id': todo.id,
                'text': todo.text,
                'completed': todo.completed
            } for todo in todos_response]

            return {
                'todos': todos,
                'paginationData': pagination_data
            }

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
            'someTodosCompleted': some_todos_completed,
            'completed': True
        }

        todos_response = db.query(Todo).order_by(Todo.id.desc())\
            .filter(Todo.completed == find_arg)\
            .offset(todos_count_data['skip_counter']*5).limit(10).all()\
            if find_arg != None\
            else db.query(Todo).offset(todos_count_data['skip_counter']*5).limit(10).all()

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
