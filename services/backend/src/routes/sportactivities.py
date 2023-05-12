from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.sportactivities as crud
from src.auth.jwthandler import get_current_user
from src.schemas.sportactivities import SportActivityOutSchema, SportActivityInSchema, UpdateSportActivity
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/sportactivities",
    response_model=List[SportActivityOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_notes():
    return await crud.get_notes()


@router.get(
    "/sportactivity/{spa_id}",
    response_model=SportActivityOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_note(spa_id: int) -> SportActivityOutSchema:
    try:
        return await crud.get_note(spa_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )


@router.post(
    "/sportactivity", response_model=SportActivityOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_note(
    note: SportActivityInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> SportActivityOutSchema:
    return await crud.create_note(note, current_user)


@router.patch(
    "/sportactivity/{spa_id}",
    dependencies=[Depends(get_current_user)],
    response_model=SportActivityOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_note(
    spa_id: int,
    sportactivity: UpdateSportActivity,
    current_user: UserOutSchema = Depends(get_current_user),
) -> SportActivityOutSchema:
    return await crud.update_note(spa_id, sportactivity, current_user)


@router.delete(
    "/sportactivity/{spa_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_note(
    spa_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_note(spa_id, current_user)
