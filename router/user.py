from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
from schemy import UserBase
from db import db_user
from db.database import get_db

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/')
def create_user(user: UserBase, db=Depends(get_db)):
    return db_user.create_user(db, user)
