import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import re

animals = ['cats','parrots','dogs']

DB_PATH = "sqlite:///my_db.sqlite3?charset=utf8"
engine = sa.create_engine(DB_PATH)


metadata = sa.MetaData()

vote_results = sa.Table('voting', metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('name', sa.Text),
    sa.Column('votes', sa.Integer)
)

def connect_db(eng):
    metadata.create_all(eng)
    session = sessionmaker(eng)
    return session()

def create_db():
    metadata.create_all(engine)
    with engine.begin() as connection:
        for animal in animals:
            statement = vote_results.insert().values(
                name = animal,
                votes = 1
            )
            connection.execute(statement)

def animals_get():
    session = connect_db(engine)
    animals = session.query(vote_results).all()
    return animals
