from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(
    Config.db_uri, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    from db.models import User

    print(f"Creating database at: {engine.url}")
    Base.metadata.create_all(bind=engine)


def get_session():
    with SessionLocal() as s:
        yield s
