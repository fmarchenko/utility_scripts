#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Jul 11, 2016"
__doc__ = """
Create a timestamped SQLite database backup, and
clean backups older than a defined number of days
"""

import argparse
import sqlite3
import shutil
import time
import os

# How old a file needs to be in order
# to be considered for being removed
NO_OF_DAYS = 7


def sqlite3_backup(dbfile, backupdir):
    """Create timestamped database copy"""

    if not os.path.isdir(backupdir):
        raise Exception("Backup directory does not exist: {}".format(backupdir))

    backup_file = os.path.join(backupdir, os.path.basename(dbfile) +
                               time.strftime("-%Y%m%d-%H%M%S"))

    connection = sqlite3.connect(dbfile)
    cursor = connection.cursor()

    # Lock database before making a backup
    cursor.execute('begin immediate')
    # Make new backup file
    shutil.copyfile(dbfile, backup_file)
    print ("\nCreating {}...".format(backup_file))
    # Unlock database
    connection.rollback()


def clean_data(backup_dir):
    """Delete files older than NO_OF_DAYS days"""

    print ("\n------------------------------")
    print ("Cleaning up old backups")

    for filename in os.listdir(backup_dir):
        backup_file = os.path.join(backup_dir, filename)
        if os.path.isfile(backup_file):
            if os.stat(backup_file).st_ctime < (time.time() - NO_OF_DAYS * 86400):
                os.remove(backup_file)
                print ("Deleting {}...".format(backup_file))


def get_arguments():
    """Parse the commandline arguments from the user"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('db_file',
                        help='the database file that needs backed up')
    parser.add_argument('backup_dir',
                         help='the directory where the backup'
                              'file should be saved')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    sqlite3_backup(args.db_file, args.backup_dir)
    clean_data(args.backup_dir)

    print ("\nBackup update has been successful.")