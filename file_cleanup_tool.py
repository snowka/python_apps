# This program performs a few simple conversions to prepare an unformatted text file for marking up.
# These include changing underscores to <ital> tags, converting ampersands to &amp, and removing blank lines.

from text_cleanup_functions import*

def opener():
    global new_file
    new_file = ""

    try:
        print("""This program performs a few simple conversions to prepare an unformatted text file for marking up.
        These include changing underscores to <ital> tags, converting ampersands to &amp, and removing blank lines.
    Place the file to be converted in the same folder as this application.
    The converted file will be named 'Converted.txt'""")
        file_loc = input(" Please enter the full name of the file to be converted, with the .txt file type at the end: ")
        file_in_process = file_loc
        conversion_options(file_in_process)
    except Exception as e:
        print(e)
        opener()


def conversion_options(file):
    """Provides the user the choice of various text processing functions"""
    question_1 = input("Convert opening underscores to <ital> tags? Y or N: ")
    # if question_1 == "Y" or "y" or "Yes" or "YES" or "yes":
    if question_1 == "Y":
        file_conversion_buffer = opening_underscore_to_ital(file)
        print(file_conversion_buffer)
    elif question_1 == "y":
        file_conversion_buffer = opening_underscore_to_ital(file)
        print(file_conversion_buffer)
    else:
        opened_file = open(file, "r")
        file_conversion_buffer = opened_file.read()

    question_2 = input("Convert closing underscores to </ital> tags? Y or N: ")
    if question_2 == "Y":
        file_conversion_buffer = closing_underscore_to_ital(file_conversion_buffer)
        print(file_conversion_buffer)
    elif question_2 == "y":
        file_conversion_buffer = closing_underscore_to_ital(file_conversion_buffer)
        print(file_conversion_buffer)
    else:
        pass

    question_3 = input("Convert ampersands to &amp? Y or N: ")
    if question_3 == "Y":
        file_conversion_buffer = ampersand_coverter(file_conversion_buffer)
        print(file_conversion_buffer)
    elif question_3 == "y":
        file_conversion_buffer = ampersand_coverter(file_conversion_buffer)
        print(file_conversion_buffer)
    else:
        pass

    question_4 = input("Remove blank lines? Y or N: ")
    if question_4 == "Y":
        file_conversion_buffer = remove_blank_lines(file_conversion_buffer)
        print(file_conversion_buffer)
    elif question_4 == "y":
        file_conversion_buffer = remove_blank_lines(file_conversion_buffer)
        print(file_conversion_buffer)
    else:
        pass

    converted_text = open("converted.txt", "a")
    x = str(file_conversion_buffer)
    converted_text.write(x)
    converted_text.close()
    print("Conversion completed. ")

try:
    opener()

except:
    print("That filename is invalid.")
    opener()
