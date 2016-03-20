import os
import argparse
from syncro.composer import Composer

composer = Composer()

def sync_in():
    '''
    sync to this system
    '''
    pass

def sync_out():
    '''
    sync to the data store
    '''
    pass


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add-file", help="add a new file to keep track of")
parser.add_argument("-r","--remove-file", help="remove a file from keeping track of")
parser.add_argument("-ls", "--list", help="list all files", action='store_true')
parser.add_argument("--sync-in", help="backup every file", action='store_true')
parser.add_argument("--sync-out", help="restore every file", action='store_true')
args = parser.parse_args()

if args.add_file:
    composer.add_file(args.add_file)
    print "done !!"

if args.remove_file:
    composer.remove_file(args.remove_file)
    print "done !!"

if args.list: composer.list_files()


if args.sync_in: composer.sync_in()

if args.sync_out: composer.sync_out()
