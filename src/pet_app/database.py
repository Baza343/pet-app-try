import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pet_app import models

load_dotenv()

postgres_database = os.getenv("DB_URL")

engine = create_engine(postgres_database)

models.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)