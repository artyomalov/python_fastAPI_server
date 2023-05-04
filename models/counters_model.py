from pydantic import BaseModel


class Counters(BaseModel):
    skip_counter: int
    pages_count: int
    todos_total_count: int
    active_todos_count: int
