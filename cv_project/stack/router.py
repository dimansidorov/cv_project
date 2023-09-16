from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from database import get_async_session
from .models import Type
from .schemas import TypeCreate, TypeRead


router = APIRouter(prefix='/stack', tags=['Stack'])


@router.get('/types', response_model=List[TypeRead])
async def get_types(session: AsyncSession = Depends(get_async_session)):
    query = select(Type.__table__)
    result = await session.execute(query)
    
    return result



@router.post('/new_type')
async def add_new_type(new_type: TypeCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(Type.__table__).values(**new_type.dict())
    await session.execute(statement)
    await session.commit()

    return {"status": "success"}

