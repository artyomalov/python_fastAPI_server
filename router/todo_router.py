"""router that contains all routs of todos and endpoints
    """

from fastapi import APIRouter
from endpoints.add_todo_endpoint import add_todo
from endpoints.complete_all_todos_endpoint import complete_all_todos
from endpoints.get_todos_endpoint import get_todos
from endpoints.delete_todo_endpoint import delete_todo
from endpoints.update_todo_endpoint import update_todo
from endpoints.delete_all_completed_todos_endpoint import delete_all_completed_todos

todo_router = APIRouter()

todo_router.add_api_route(path='/', endpoint=get_todos, methods=['GET'])
todo_router.add_api_route(path='/', endpoint=add_todo, methods=['POST'])
todo_router.add_api_route(
    path='/{id}', endpoint=delete_todo, methods=['DELETE'])
todo_router.add_api_route(
    path='/{id}', endpoint=update_todo, methods=['PATCH'])
todo_router.add_api_route(
    path='/', endpoint=complete_all_todos, methods=['PATCH'])
todo_router.add_api_route(
    path='/', endpoint=delete_all_completed_todos, methods={'DELETE'})
