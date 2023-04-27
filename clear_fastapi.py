# from enum import Enum
# from typing import List, Optional
# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI(title="Trading App")


# class Rank(Enum):
#     newbie = "newbie"
#     expert = "expert"


# class Degree(BaseModel):
#     rank: Rank


# class User(BaseModel):
#     id: int
#     role: str = Field(max_length=20)
#     name: str
#     age: int = Field(ge=0)
#     degree: Optional[Degree]


# fake_users: List[User] = [
#     {
#         'id': 1,
#         'role': 'admin',
#         'name': 'Bob',
#         'age': 23,
#     },
#     {
#         'id': 2,
#         'role': 'admin',
#         'name': 'Bob',
#         'age': 23,
#         'degree': {
#             'rank': 'expert',
#         }},
#     {
#         'id': 3,
#         'role': 'admin',
#         'name': 'Bob',
#         'age': 23,
#         'degree': {
#             'rank': 'expert',
#         }},
#     {
#         'id': 4,
#         'role': 'admin',
#         'name': 'Bob',
#         'age': 23,
#         'degree': {
#             'rank': 'expert',
#         }},
# ]


# @app.get('/users/{user_id}', response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user["id"] == user_id]


# @app.post('/users/')
# def add_user(users: List[User]):
#     fake_users.extend(users)
#     return {'status': 200, "data": fake_users}
