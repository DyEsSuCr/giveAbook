from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    hashed_password: str


class UserBase(UserSchema):
    id: int
