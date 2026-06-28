from pydantic import BaseModel
from datetime import datetime
import uuid


class Todo(BaseModel):
    task: str
    id: str = str(uuid.uuid4())
    date_created: str = str(datetime.now())
    is_completed: bool = False
