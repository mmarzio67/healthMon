from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import SportActivities

# Create pydantic models from tortoise models
# schema for creating new sport activities
SportActivityInSchema = pydantic_model_creator(
    SportActivities, name="SportActivityIn", exclude=["author_id"], exclude_readonly=True)

# schema for creating new retrieving sport activities
SportActivityOutSchema = pydantic_model_creator(
    SportActivities, name="SportActivity", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)

# Class for updating a sport activity
class UpdateSportActivity(BaseModel):
    title: Optional[str]
    content: Optional[str]