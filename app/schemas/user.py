from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str
    age: int
    initial_weight: float

class UserCreate(UserBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "johndoe@example.com",
                "username": "John Doe",
                "age": 30,
                "initial_weight": 70.5,
                "password": "password123"
            }
        }
    }

class UserUpdate(BaseModel):
    email: EmailStr = None
    username: str = None
    age: int = None
    initial_weight: float = None

    model_config = ConfigDict(from_attributes = True)

class UserOut(UserBase):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes = True)

class UserInDB(UserOut):
    hashed_password: str

class LoginData(BaseModel):
    email: EmailStr
    password: str