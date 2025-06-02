from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    # 'orm_mode' has been renamed to 'from_attributes' in pydantic V2, so created this
    model_config = ConfigDict(from_attributes=True) 