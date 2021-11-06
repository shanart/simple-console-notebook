import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Process some integers.')
from notebook.notes import create_note, get_note, find_note, delete_note, update_note
from notebook.db import init_db


parser.add_argument("-g", "--get", help="Get note", type=int)
parser.add_argument("-c", "--create", help="Create new note", type=str)
parser.add_argument("-u", "--update", help="Update note. Require using -t/--text flag to fill updated note content", type=int)
parser.add_argument("-t", "--text", help="Content. Require using -u/--update flag to get updated note id", type=str)
parser.add_argument("-s", "--search", help="Search note", type=str)
parser.add_argument("-i", "--init", help="Init database", action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    if args.get:
        print("Getting note with id: {}".format(args.get))
    elif args.search:
        print("Searching notes contains '{}' in content".format(args.search))
    elif args.create:
        print("Creating note with content: {}".format(args.create))
    elif args.update and args.text:
        print("Updating note {}. Content: {}".format(args.update, args.text))
    elif args.init:
        print("Note database initialized")

    # pprint(update_note(3, 'this is second content'))
