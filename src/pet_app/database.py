from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pet_app import models

sqlite_database = "sqlite:///tasks.db"

engine = create_engine(sqlite_database)

models.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)