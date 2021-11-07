# Simple console notebook

### Build
```
$ python -m build
```


### Usage
```
$ python run.py -h


usage: run.py [-h] [-g GET] [-c CREATE] [-d DELETE] [-u UPDATE] [-t TEXT] [-s SEARCH] [-i]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -g GET, --get GET     Get note
  -c CREATE, --create CREATE
                        Create new note
  -d DELETE, --delete DELETE
                        Delete note by id
  -u UPDATE, --update UPDATE
                        Update note. Require using -t/--text flag to fill updated note content
  -t TEXT, --text TEXT  Content. Require using -u/--update flag to get updated note id
  -s SEARCH, --search SEARCH
                        Search note
  -i, --init            Init database
```
