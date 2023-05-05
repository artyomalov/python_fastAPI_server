"""main file of the app
    """
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.session import engine
from database.basemodel import Base
from router.todo_router import todo_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="todo_api",
    version='0.0.1'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# localhost:8000/api/todos -> my-site.com/api/todos
# localhost:8000/todos -> back.my-site.com/todos

# localhost:3000/todos -> my-site.com/todos


app.include_router(
    todo_router,
    prefix="/api",
)
# app.include_router(user_router)
# app.include_router(review_router)
# app.include_router(item_router)
