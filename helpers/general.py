import os
import pathlib
import sys
import textwrap

from ._utilities import print_block

def get_home_directory() -> pathlib.Path:
    # In this context, "home directory" is the directory
    # containing the script file that launched this Python process.
    mainfile = sys.argv[0]
    home_directory = pathlib.Path(mainfile).parent
    return home_directory


def inform_no_user_file_found(scriptname):
        home_dir = get_home_directory()
        print("ERROR.")
        print("This script,")
        print()
        print(f"    {scriptname}")
        print()
        print_block("needs you to provide a user file, typically the list of extensions downloaded from the PBX. It looks for that file in its home directory, currently")
        print()
        print(f"    {home_dir}")
        print()
        print_block("Specifically, it looks for a '.csv' file beginning with 'users-'. No such file was found, and therefore this script cannot continue.")
        print() # Empty line
        input("Press enter to close this screen.")


def reset_home_directory():
    os.chdir(get_home_directory())
