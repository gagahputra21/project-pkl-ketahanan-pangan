from sqlalchemy import Column, String, Boolean
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
