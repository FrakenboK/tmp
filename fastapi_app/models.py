from sqlalchemy import Table, Column, Integer, String
from database import metadata, engine

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(50), unique=True)
)

metadata.create_all(engine)