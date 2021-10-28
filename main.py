# Mail Merge Program

####_____________________####
####Created by 4bd3ss4m4d####
####_____________________####

from pathlib import Path

DATA_FOLDER = Path("D:\\Workspace\Python\\Intermediate level Projects\\Mail Merge "
                   "Project\\main")
                   
LETTER_FOLDER = DATA_FOLDER / "D:\\Workspace\\Python\\100 Days Python Bootcamp\\Mail " \
                              "Merge Project\\Input\\Letters\\starting_letter.txt "

NAMES_FOLDER = DATA_FOLDER / "D:\\Workspace\\Python\\Intermediate level Projects\\Mail " \
                             "Merge Project\\Input\\Names\\invited_names.txt "

DESTINATION_FOLDER = DATA_FOLDER / "D:\\Workspace\\Python\\Intermediate level Projects\Mail " \
                                   "Merge Project\\Output\\ReadyToSend\\done_letters.txt "


def main():
    # Open original letter
    with open(LETTER_FOLDER, 'r') as letter_file:
        # Open names of the invited guests
        with open(NAMES_FOLDER, 'r') as names_file:
            # Create the destination file
            with open(DESTINATION_FOLDER, 'w') as destination_file:
                # Get the original letter
                original_letter = letter_file.read()
                # Get the first name
                name = names_file.readline()
                # Loop throw all the names of the names_file
                while name != '':
                    # strip the \n from name
                    name = name.rstrip('\n')

                    #
                    done_letter = original_letter
                    done_letter = done_letter.replace('[name]', name)

                    destination_file.write(done_letter)
                    destination_file.write('__________________________\n')

                    # Get the next name of the names_file
                    name = names_file.readline()
    print("Letters successfully created.")


main()

