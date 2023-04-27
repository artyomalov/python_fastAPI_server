"""main file of the app
    """
from fastapi import FastAPI
import uvicorn
from database.session import engine
from database.basemodel import Base
from router.todo_router import todo_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(todo_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# # @app.on_event("startup")
# async def startup():
#     await database.connect()  # creating connection to db. import db frpm db.base.py


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()  # closing connection to db


# from sqlalchemy import desc
# someselect.order_by(desc(table1.mycol))
