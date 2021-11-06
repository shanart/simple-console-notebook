from operator import or_
from sqlalchemy import select, insert, delete, update
from notebook.db import connection, notes


def create_note(content):
    query = insert(notes).values(content=content)
    connection.execute(query)
    return "note saved"


def get_note(note_id=None):
    query = select([notes]).where(notes.c.note_id == note_id)
    result = connection.execute(query).fetchone()
    return result


def find_note(search_str):
    query = select([notes]).where(notes.c.content.like('%{}%'.format(search_str)))
    result = connection.execute(query).fetchall()
    return result


def delete_note(id):
    query = delete(notes).where(notes.c.note_id==id)
    connection.execute(query)
    return 'note deleted'


def update_note(id, content):
    query = update(notes).where(notes.c.note_id==id).values(content=content)
    connection.execute(query)
    return 'note saved'
