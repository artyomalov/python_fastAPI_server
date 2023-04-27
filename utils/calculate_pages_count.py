"""_summary_
Returns:
    _type_: _description_
"""
import math
from pydantic import BaseModel


class Counters(BaseModel):
    skip_counter: int
    pages_count: int
    todos_total_count: int
    active_todos_count: int


def calculate_pages_count(filter_value: str, page_number: int, data_base, model) -> Counters:
    """_summary_

    Args:
        filter_value (str): value of filter that got from  query string
        page_number (int): page number that got from  query string
        data_base (_type_): SessionLocal class object, used to get access to the db
        model (_type_): database's table's model
    Returns:
        Counters: {
            skip_counter: int
            pages_count: int
            todos_total_count: int
            active_todos_count: int
        }
    """
    todos_total_count = data_base.query(model).count()
    active_todos_count = data_base.query(
        model).filter(model.completed == False).count()
    todos_count = todos_total_count
    if filter_value != 'all':
        todos_count = active_todos_count if filter_value == 'active' else data_base.query(
            model).filter(model.completed == True).count()

    unrounded_count = todos_count / 5

    pages_count = unrounded_count if unrounded_count % 5 == 0 else int(math.ceil(
        unrounded_count))

    skip_counter = int(page_number) - 1

    todos_count_data: Counters = {
        'skip_counter': 0,
        'pages_count': pages_count,
        'todos_total_count': todos_total_count,
        'active_todos_count': active_todos_count,
    }
    todos_count_data['skip_counter'] = skip_counter

    if pages_count <= 1:
        skip_counter = 0
        todos_count_data['skip_counter'] = skip_counter

    if int(page_number) > pages_count:
        skip_counter = 0 if int(pages_count) == 0 else int(pages_count) - 1
        todos_count_data['skip_counter'] = skip_counter

    return todos_count_data
