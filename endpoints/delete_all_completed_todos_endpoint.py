from fastapi.responses import JSONResponse
from database.session import db
from database.basemodel import Todo
from utils.calculate_pages_count import calculate_pages_count
from utils.get_find_arg import get_find_arg


def delete_all_completed_todos(filterValue: str):
    try:
        result = db.query(Todo).filter(Todo.completed == True).delete(
            synchronize_session='fetch')
        db.commit()
        if not result:
            raise Exception('DB error')

        find_arg = get_find_arg(filter_value=filterValue)

        todos_count_data = calculate_pages_count(
            filter_value=filterValue, page_number=1, data_base=db, model=Todo)

        some_todos_completed = todos_count_data['todos_total_count'] - \
            todos_count_data['active_todos_count'] > 0

        pagination_data = {
            'todosTotalCount': todos_count_data['todos_total_count'],
            'activeTodosCount': todos_count_data['active_todos_count'],
            'pagesCount': todos_count_data['pages_count'],
            'someTodosCompleted': some_todos_completed
        }

        todos_response = db.query(Todo).filter(Todo.completed == find_arg).offset(
            todos_count_data['skip_counter']*5).limit(10).all()

        todos = [{'id': todo.id, 'text': todo.text,
                  'completed': todo.completed} for todo in todos_response]
        return {
            'todos': todos,
            'paginationData': pagination_data
        }

    except Exception as err:
        return JSONResponse({'error': err}, status_code=500)
