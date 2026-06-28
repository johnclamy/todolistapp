from fastapi import APIRouter
from model.todo import Todo
import data.todo as service


router = APIRouter(prefix = '/api/v1/todos')


@router.get('/')
async def get_todos() -> list[Todo]:
    todos = await service.get_todos()

    return todos


@router.post('/')
async def add_todo(todo: Todo) -> dict[str, str]:
    await service.add_todo(todo)

    return {'message': 'Todo added successfully'}


@router.put('/{todoId}')
async def update_todo(todoId: str) -> dict[str, str]:
    await service.update_todo(todoId)

    return {'message': 'Todo updated successfully'}


@router.delete('/{todoId}')
async def delete_todo(todoId: str) -> dict[str, str]:
    await service.delete_todo(todoId)

    return {'message': 'Todo deleted successfully'}
