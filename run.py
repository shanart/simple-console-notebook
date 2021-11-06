from pprint import pprint

from notebook.notes import create_note, get_note, find_note, delete_note, update_note
from notebook.db import init_db


if __name__ == '__main__':
    pprint(update_note(3, 'this is second content'))
