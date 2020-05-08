import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import re

animals = ['cats','parrots','dogs']
DB_PATH = "sqlite:///my_db.sqlite3?charset=utf8"
engine = sa.create_engine(DB_PATH)
Base = declarative_base()

metadata = sa.MetaData()

vote_results = sa.Table('voting', metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('name', sa.Text),
    sa.Column('votes', sa.Integer)
)

def connect_db():
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def create_db():
    Base.metadata.create_all(engine)
    with engine.begin() as connection:
        for animal in animals:
            statement = vote_results.insert().values(
                name=animal,
                votes=0
            )
            connection.execute(statement)

def animals_get():
    if not engine.dialect.has_table(engine, vote_results):
        create_db()
    else:
            session = connect_db()

    animals = session.query(vote_results).all()
    return animals
