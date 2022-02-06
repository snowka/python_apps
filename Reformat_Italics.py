# This program opens a file and reformats the italics from underscores to <ital> tags.

import re


def opener():
    global new_file
    new_file = ""
    global file_loc
    try:
        print("""This program converts the italicization in a text file from
    underscores to <ital> tags.
    Place the file to be converted in the same folder as this application.
    The converted file will be named 'Converted.txt'""")
        file_loc = input(" Please enter the full name of the file to be converted, with the .txt file type at the end: ")
        underscore_to_italics(file_loc)
    except Exception as e:
        print(e)
        opener()


def underscore_to_italics(text_to_correct):
    """Changes the form of italicization in a string."""
    opened_file = open(text_to_correct, "r")
    file_buffer = opened_file.read()
    # the expression is a regex lookahead that finds any underscore followed by a word
    file_buffer1 = re.sub(r"_(?=\w)", " <ital>", file_buffer)
    # the expression is a regex lookbehind that finds any underscore preceded by a word
    file_buffer2 = re.sub(r"(?<=\w)_", "</ital>", file_buffer1)
    print(file_buffer2)
    converted_text = open("converted.txt", "a")
    x = str(file_buffer2)
    converted_text.write(x)
    opened_file.close()
    converted_text.close()
    print("Conversion completed. ")

try:
    opener()

except:
    print("That filename is invalid.")
    opener()
