from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Table, DateTime

metadata = MetaData()

notes = Table(
    'notes', metadata,
    Column('note_id', Integer(), primary_key=True),
    Column('title', String(64), nullable=False, unique=True),
    Column('content', Text(), nullable=True),

    # Date fields
    Column('reminder_date', DateTime(), nullable=True),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

engine = create_engine('sqlite:///db.sqlite3')
metadata.create_all(engine)
connection = engine.connect()
