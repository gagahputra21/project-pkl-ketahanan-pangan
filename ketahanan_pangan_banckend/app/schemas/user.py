from pydantic import BaseModel
from typing import Optional

# Untuk response ke frontend
class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        orm_mode = True  # Agar bisa di-convert dari SQLAlchemy object

# Untuk data dari DB (termasuk hashed_password)
class UserInDB(User):
    hashed_password: str
