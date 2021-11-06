from sqlalchemy import select, insert, delete, update
from db import connection, notes


def create_note(note_title, note_text=None):
    query = insert([notes]).values(
        notes.c.title == note_title,
        notes.c.content == note_text
    )
    connection.execute(query)
    return "note saved"


def get_note(note_id=None):
    query = select([notes]).where(notes.c.note_id == note_id)
    result = connection.execute(query).fetchone()
    return result

# create_note
# find_note
# delete_note
# update_note


if __name__ == '__main__':
    create_note(note_title='test', note_text='test test')
    get_note(1)

