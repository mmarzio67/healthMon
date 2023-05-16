from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.db import users as Users 

# Create pydantic models from sqlalchemy models

# schema for creating new users
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# schema for retrieving users outside the application (API)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

# schema for retrieving users within the application (validation of users)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)