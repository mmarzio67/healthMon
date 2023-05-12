from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import SportActivities
from src.schemas.sportactivities import SportActivityOutSchema
from src.schemas.token import Status


async def get_sportActivity():
    return await SportActivityOutSchema.from_queryset(SportActivities.all())


async def get_sportActivity(sportActivity_id) -> SportActivityOutSchema:
    return await SportActivityOutSchema.from_queryset_single(SportActivities.get(id=sportActivity_id))


async def create_sportActivity(sportActivity, current_user) -> SportActivityOutSchema:
    sportActivity_dict = sportActivity.dict(exclude_unset=True)
    sportActivity_dict["athlete_id"] = current_user.id
    sportActivity_obj = await SportActivities.create(**sportActivity_dict)
    return await SportActivityOutSchema.from_tortoise_orm(sportActivity_obj)


# only the athlete that performed the activity can update it
async def update_sportActivity(sportActivity_id, sportActivity, current_user) -> SportActivityOutSchema:
    try:
        db_sportActivity = await SportActivityOutSchema.from_queryset_single(SportActivities.get(id=sportActivity_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Sport activity {sportActivity_id} not found")

    if db_sportActivity.athlete.id == current_user.id:
        await SportActivities.filter(id=sportActivity_id).update(**sportActivity.dict(exclude_unset=True))
        return await SportActivityOutSchema.from_queryset_single(SportActivities.get(id=sportActivity_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")

# only the athlete that performed the activity can update it
async def delete_sportActivity(sportActivity_id, current_user) -> Status:
    try:
        db_sportActivity = await SportActivityOutSchema.from_queryset_single(SportActivities.get(id=sportActivity_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Sport activity {sportActivity_id} not found")

    if db_sportActivity.athlete.id == current_user.id:
        deleted_count = await SportActivities.filter(id=sportActivity_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Sport actvity {sportActivity_id} not found")
        return Status(f"Deleted sport activity {sportActivity_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")