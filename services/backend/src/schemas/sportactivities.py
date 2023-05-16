from typing import Optional

from pydantic import BaseModel

from src.database.db import sportactivities as SportActivities

# Create pydantic models from tortoise models
# schema for creating new sport activities
SportActivityInSchema = pydantic_model_creator(
    SportActivities, name="SportActivityIn", exclude=["athlete_id"], exclude_readonly=True)

# schema for creating new retrieving sport activities
SportActivityOutSchema = pydantic_model_creator(
    SportActivities, name="SportActivity", exclude =[
      "modified_at", "athlete.password", "athlete.created_at", "athlete.modified_at"
    ]
)

# Class for updating a sport activity
class UpdateSportActivity(BaseModel):
    title: Optional[str]
    content: Optional[str]