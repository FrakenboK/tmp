from sqlalchemy import MetaData, create_engine
from databases import Database

DATABASE_URL = "sqlite:///./data/test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)