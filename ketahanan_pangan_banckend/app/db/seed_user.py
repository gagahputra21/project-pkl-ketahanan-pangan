from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_initial_user():
    db: Session = SessionLocal()
    user = db.query(User).filter(User.username == "admin@example.com").first()
    if not user:
        new_user = User(
            username="admin@example.com",
            full_name="Admin User",
            hashed_password=pwd_context.hash("admin123"),  # ganti sesuai keinginan
            disabled=False
        )
        db.add(new_user)
        db.commit()
        print("User admin@example.com berhasil ditambahkan.")
    else:
        print("User sudah ada.")
    db.close()

if __name__ == "__main__":
    create_initial_user()
