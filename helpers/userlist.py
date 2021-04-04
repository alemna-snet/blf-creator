import csv
from pathlib import Path


def choose_userlist_file(list_of_files: list):
    # If there are multiple possible files, we'll assume we want the latest one,
    # and we'll also assume that its file name contains the date, and also
    # assume the OS has sorted it towards the end of the directory so it was
    # probably the last file put into "possible_userlist_files".
    #
    # Yeah, that's a lot of assumptions, but implement better logic later. Put that
    # on the TODO list.
    return list_of_files[-1]

def find_userlist_file_in(target_directory: Path):
    # TODO: Make it recursively search subdirectories
    possible_userlist_files: list = []
    valid_filetypes: list = [".csv"]
    for item in target_directory.iterdir():
        if item.is_file() and item.suffix in valid_filetypes and item.name[0:6] == "users-":
            possible_userlist_files.append(item)

    number_of_possible_files = len(possible_userlist_files)
    if number_of_possible_files == 0:
        raise FileNotFoundError 
    elif number_of_possible_files == 1:
        userlist_file = possible_userlist_files[0]
        return userlist_file
    else:
        return possible_userlist_files


def get_all_users(target_file: Path):
    user_dictionary = {}
    with open(target_file) as userfile:
        userlist = csv.reader(userfile)
        for row in userlist:
            if row == 0:
                pass  # skip the header
            else:
                name, ext = row[0], row[2]
                user_dictionary[ext] = name
        return user_dictionary
