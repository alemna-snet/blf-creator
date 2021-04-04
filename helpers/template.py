import csv

from ._utilities import is_blank

def parse(file_to_parse):
    mod_1_starts_on: int = 1
    mod_2_starts_on: int = 13
    mod_3_starts_on: int = 25
    # no blf info in these lines...
    lines_to_skip = (mod_1_starts_on, mod_2_starts_on, mod_3_starts_on) 


    raw_blfs: dict = {}
    # starting with module 1...
    # left blfs
    with open(file_to_parse) as file_object:
        file_contents = csv.reader(file_object)
        # load file contents into a list of lists, which will 
        # look like:
        #
        #   raw_blf_extensions[
        #       row1[cell, cell, cell... ] 
        #       row2[cell, cell, cell... ] 
        #       ...
        #   ]
        #
        # Then go through each row and add the cells with the info 
        # for the left-side blfs to the list "raw_blfs"
        current_blf_number = 1
        for row in file_contents:
            if is_blank(row):
                pass
            elif file_contents.line_num in lines_to_skip:
                pass
            elif file_contents.line_num in range(mod_1_starts_on, mod_2_starts_on):  # mod 1
                if current_blf_number > 20:
                    raise IndexError
                left_blf_number = current_blf_number
                right_blf_number = left_blf_number + 10

                # TODO: write an explanation of this
                left_blf_ext, left_blf_name  = row[0], row[1]
                right_blf_name, right_blf_ext = row[2], row[3]
                # and add to the dictonary of raw blfs
                raw_blfs[left_blf_number] = (left_blf_ext, left_blf_name)
                raw_blfs[right_blf_number] = (right_blf_ext, right_blf_name)

                # and increment for the next loop
                current_blf_number = current_blf_number + 1
            elif file_contents.line_num in range(mod_2_starts_on, mod_3_starts_on):  # mod 2
                if current_blf_number < 20:
                    current_blf_number = 21  # I KNOW, I KNOW, I'M A KLUDGE
                if current_blf_number > 40:
                    raise IndexError
                left_blf_number = current_blf_number
                right_blf_number = left_blf_number + 10

                # TODO: write an explanation of this
                left_blf_ext, left_blf_name  = row[0], row[1]
                right_blf_name, right_blf_ext = row[2], row[3]
                # and add to the dictonary of raw blfs
                raw_blfs[left_blf_number] = (left_blf_ext, left_blf_name)
                raw_blfs[right_blf_number] = (right_blf_ext, right_blf_name)

                # and increment for the next loop
                current_blf_number = current_blf_number + 1
            else:  # mod 3
                if current_blf_number < 40:
                    current_blf_number = 41  # I KNOW, I KNOW, I'M A KLUDGE
                if current_blf_number > 60:
                    raise IndexError
                left_blf_number = current_blf_number
                right_blf_number = left_blf_number + 10

                # TODO: write an explanation of this
                left_blf_ext, left_blf_name  = row[0], row[1]
                right_blf_name, right_blf_ext = row[2], row[3]
                # and add to the dictonary of raw blfs
                raw_blfs[left_blf_number] = (left_blf_ext, left_blf_name)
                raw_blfs[right_blf_number] = (right_blf_ext, right_blf_name)

                # and increment for the next loop
                current_blf_number = current_blf_number + 1
        
        # Next up, sorting the raw blfs.
        # Dictionaries in Python aren't able to be sorted, but it's
        # easy enough to make a new dictionary built by accessing
        # the raw_blf{} dictionary key values sequentially...
        sorted_blfs: dict = {}
        for integer in range(1, 61):
            sorted_blfs[integer] = raw_blfs[integer]
        return sorted_blfs


def autofill(blf_dict: dict, user_dict: dict):
    """Accepts a dictonary of BLFs and a dictionary of users. Where there is 
    partial information (empty extension numbers or empty names) in the BLF 
    dictionary, this function will look in the user dictionary for matching 
    info it can use to fill in.
    """
    for blf_number in blf_dict:
        blf = blf_dict[blf_number]
        destination, label = blf[0], blf[1]
        if destination == "":
            # This is a bit tricky, because technically there can be more than one extension with the same username.
            possible_destinations = [extension for extension, user_name in user_dict.items() if user_name == label]
            number_of_possible_destinations = len(possible_destinations)
            if number_of_possible_destinations > 1:
                pass
                # raise Exception
                # TODO: Make this give useful feedback to the user 
            elif number_of_possible_destinations == 1:
                # Since there's only one possible destination,
                # we assume it's the intended destination.
                assumed_destination = possible_destinations[0]
                blf = (assumed_destination, label)
                blf_dict[blf_number] = blf
            else: 
                pass  # do nothing
        elif label == "":
            blf = (destination, user_dict[destination])
            blf_dict[blf_number] = blf
        else:
            pass
    return blf_dict