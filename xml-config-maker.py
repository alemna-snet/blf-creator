# import csv
from datetime import datetime
from pathlib import Path
import traceback

import helpers.userlist as userlist
import helpers.template as template
import helpers.syntax as syntax
import helpers.general as gen


if __name__ == "__main__":
    try:
        gen.reset_home_directory()
        current_working_directory = Path.cwd()

        # LOAD USER DICTIONARY
        try:
            userfile = userlist.find_userlist_file_in(current_working_directory)
        except FileNotFoundError:
            name_of_this_script = __file__
            gen.inform_no_user_file_found(name_of_this_script)
        # If there are multiple possible user dictionary files...
        if isinstance(userfile, list):
            userfile = userlist.choose_userlist_file(userfile)
        users = userlist.get_all_users(userfile)

        # CREATE BLF DICTIONARY
        # This is a two-stage process. The first stage 'template.parse()' opens the 'template file' and 
        # grabs whatever data is in the predetermined fields. The second stage looks at the data in the 
        # 'users' dictionary (see above) and attempts to fill in any blanks.
        template_file = "Expansion Module Template.csv"
        parsed_blfs = template.parse(template_file)  # stage I
        autofilled_blfs = template.autofill(parsed_blfs, users)  # stage II

        # Generate syntax
        full_syntax = []
        for blf_number in autofilled_blfs:
            extension, user = autofilled_blfs[blf_number]
            line = blf_number
            full_syntax.append(syntax.get_sidecar_blf_syntax(line, extension, user))
        now = datetime.now()
        date_time_string = now.strftime("%Y_%m_%d-%H_%M_%S")
        syntax_file_name = f"blf_xml_{date_time_string}.txt"
        with open(syntax_file_name, mode="x") as syntax_file:
            syntax_file.writelines(["features.enhanced_dss_keys.enable = 1", "\n"])
            for entry in full_syntax:
                if entry is None:
                    pass
                else:
                    for line in entry:
                        syntax_file.write(line + "\n")
        print("Done. Output file is:")
        print(f"    {syntax_file_name}")
        print()
        while True:
            input("Press enter to close this screen.")
    
    # If we run into an error...
    except Exception as e:
        print("ERROR.")
        print()
        traceback.print_exc()
        print()
        print("PLEASE COPY AND PASTE THIS ERROR MESSAGE AND SEND IT TO WHOEVER")
        print("MAINTAINS THIS SCRIPT.")
        print()
        # And then create an endless loop to keep the console window open 
        # until the user closes it.
        while True:
            input()

