from model.todo import Todo


# Sample data, to be replaced by a real database
_todos: list[Todo] = [
    Todo(
        task='Learn Python',
        id='d48529c7-a452-4b02-94a6-8d53427590c7',
        date_created='2026-06-28 17:15:18.159129',
        is_completed=True,
    ),    
    Todo(
        task='Clean the house',
        id='3d58c648-6dc6-449a-8111-bf4a40fb24d8',
        date_created='2026-06-28 17:15:18.159129',
        is_completed=False,
    ),
    Todo(
        task='Buy groceries',
        id='237e7324-9cb8-40b6-bbcf-3186838ec415',
        date_created='2026-06-28 17:18:11.159129',
        is_completed=False,
    ),
]


# CRUD operations

async def get_todos() -> list[Todo]:
    ''' READ all todos '''
    return _todos


async def add_todo(todo: Todo) -> None:
    ''' CREATE a new todo '''
    _todos.append(todo)


async def update_todo(todoId: str) -> None:
    ''' UPDATE a todo '''
    pass
    
    
async def delete_todo(todoId: str) -> None:
    ''' DELETE a todo '''
    pass
