from pydantic import BaseModel


class Todo(BaseModel):
    id: str
    task: str
    is_completed: bool = False
    date_created: str