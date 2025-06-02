from app.db.database import Base, engine
from app.models import user  # pastikan model di-import agar dikenali

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
