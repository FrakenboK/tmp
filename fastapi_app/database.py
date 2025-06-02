from sqlalchemy import MetaData, create_engine
from databases import Database
import os 

DATABASE_URL = os.getenv("DB_PATH", "sqlite:///./data/test.db")

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)