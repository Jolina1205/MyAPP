from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future= True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future= True)

Base = declarative_base()

#DB Utilities
def get_DB():
    DB = SessionLocal()
    try:
        yield DB
    finally:
        DB.close()    