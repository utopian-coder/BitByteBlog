from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    email: EmailStr = Field(..., unique=True)
    password: str