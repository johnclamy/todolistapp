from pydantic import BaseModel


class Todo(BaseModel):
    id: str
    task: str
    date_created: str
    is_completed: bool = False