"""router that contains all routs of todos and endpoints
    """

from typing import Annotated
from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from database.basemodel import Todo
from database.session import db
from endpoints.add_todo_endpoint import add_todo
from endpoints.complete_all_todos_endpoint import complete_all_todos
from endpoints.get_todos_endpoint import get_todos
from endpoints.delete_todo_endpoint import delete_todo
from endpoints.update_todo_endpoint import update_todo
from endpoints.delete_all_completed_todos_endpoint import delete_all_completed_todos
from models.add_todo_model import AddTodoRequestBody
from utils.calculate_pages_count_servise import calculate_pages_count
from utils.get_find_arg_servise import get_find_arg
from utils.get_todos_servise import get_todos_handler


# def common_params():
#     return {"x": 1}
# , dependencies=[Depends(common_params)]

todo_router = APIRouter(
    tags=['todos'],
    prefix="/todos",
)


@todo_router.get("/", tags=['todos'])
async def get_todos_wrapper(filterValue: str, pageNumber: int):
    return get_todos(filterValue=filterValue, pageNumber=pageNumber)


@todo_router.post("/", tags=['todos'])
async def add_todos_wrapper(body: AddTodoRequestBody, filterValue: str, pageNumber: int):
    return add_todo(body=body, filterValue=filterValue, pageNumber=pageNumber)


@todo_router.patch("/{id}", tags=['todos'])
async def update_todo_wrapper(id: int, body=Body()):
    return update_todo(id=id, body=body)


@todo_router.patch("/", tags=['todos'])
async def update_all_todos_wrapper(filterValue: str):
    return complete_all_todos(filterValue=filterValue)


@todo_router.delete("/{id}", tags=['todos'])
async def delete_todo_wrapper(id: int):
    return delete_todo(id=id)


@todo_router.delete("/", tags=['todos'])
async def delete_completed_todos_wrapper(filterValue: str):
    return delete_all_completed_todos(filterValue=filterValue)


# @todo_router.get("/", tags=['todos'])
# async def get_todos_wrapper(common_params: Annotated[dict, Depends(common_params)], filterValue: str = all, pageNumber: int = 1):
#     try:

#         find_arg = get_find_arg(filterValue)
#         todos_count_data = calculate_pages_count(
#             filter_value=filterValue,
#             page_number=pageNumber,
#             data_base=db,
#             model=Todo
#         )

#         some_todos_completed = todos_count_data['todos_total_count'] - \
#             todos_count_data['active_todos_count'] > 0

#         pagination_data = {
#             'todosTotalCount': todos_count_data['todos_total_count'],
#             'activeTodosCount': todos_count_data['active_todos_count'],
#             'pagesCount': todos_count_data['pages_count'],
#             'someTodosCompleted': some_todos_completed
#         }

#         todos_response = get_todos_handler(
#             find_arg=find_arg,
#             data_base=db,
#             model=Todo,
#             skip_counter=todos_count_data['skip_counter']
#         )

#         todos = [{
#             '_id': todo.id,
#             'text': todo.text,
#             'completed': todo.completed
#         } for todo in todos_response]
#         return JSONResponse({
#             'todos': todos,
#             'paginationData': pagination_data
#         })

#     except Exception as err:
#         return err


# todo_router.add_api_route(path='/', endpoint=get_todos, methods=['GET'])
# todo_router.add_api_route(path='/', endpoint=add_todo, methods=['POST'])
# todo_router.add_api_route(
#     path='/{id}', endpoint=delete_todo, methods=['DELETE'])
# todo_router.add_api_route(
#     path='/{id}', endpoint=update_todo, methods=['PATCH'])
# todo_router.add_api_route(
#     path='/', endpoint=complete_all_todos, methods=['PATCH'])
# todo_router.add_api_route(
#     path='/', endpoint=delete_all_completed_todos, methods={'DELETE'})
