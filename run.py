import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Process some integers.')
from notebook.notes import create_note, get_note, find_note, delete_note, update_note
from notebook.db import init_db


parser.add_argument("-g", "--get", help="Get note", type=int)
parser.add_argument("-c", "--create", help="Create new note", type=str)
parser.add_argument("-d", "--delete", help="Delete note by id", type=int)
parser.add_argument("-u", "--update", help="Update note. Require using -t/--text flag to fill updated note content", type=int)
parser.add_argument("-t", "--text", help="Content. Require using -u/--update flag to get updated note id", type=str)
parser.add_argument("-s", "--search", help="Search note", type=str)
parser.add_argument("-i", "--init", help="Init database", action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    if args.get:
        print(get_note(args.get))
    elif args.delete:
        print(delete_note(args.delete))
    elif args.search:
        print(find_note(args.search))
    elif args.create:
        print(create_note(args.create))
    elif args.update and args.text:
        print(update_note(args.update, args.text))
    elif args.init:
        print(init_db())
