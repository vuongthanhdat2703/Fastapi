from sqlalchemy import Table, Column
from config.db import meta,engine
from sqlalchemy.sql.sqltypes import Integer,String,INT

student = Table (
    'student',meta,
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('age', INT),
    Column('country', String(255))
)

meta.create_all(engine)