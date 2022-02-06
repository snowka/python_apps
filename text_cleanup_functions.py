# A collection of functions for preparing a text file for markup
import re


def opening_underscore_to_ital(text_to_correct):
    """Uses a regex lookahead to convert an underscore before a word to an <ital> tag"""
    opened_file = open(text_to_correct, "r")
    file_buffer = opened_file.read()
    # the expression is a regex lookahead that finds any underscore followed by a word
    file_buffer1 = re.sub(r"_(?=\w)", " <ital>", file_buffer)
    opened_file.close()
    return file_buffer1


def closing_underscore_to_ital(file_conversion_buffer):
    """Uses a regex lookbehind to convert an underscore after a word to an </ital> tag"""
    # the expression is a regex lookahead that finds any underscore followed by a word
    file_buffer1 = re.sub(r"(?<=\w)_", " </ital>", file_conversion_buffer)
    return file_buffer1


def ampersand_coverter(file_conversion_buffer):
    """Uses the replace method to convert ampersands to &amp"""
    file_conversion_buffer = file_conversion_buffer.replace("&", "&amp")
    file_buffer1 = file_conversion_buffer
    return file_buffer1


def open_carat_character_entity_reference(file_conversion_buffer):
    """Uses the replace method to replace a carat with its character entity reference"""
    file_conversion_buffer = file_conversion_buffer.replace("<", "&lt")
    file_buffer1 = file_conversion_buffer
    return file_buffer1


def remove_blank_lines(file_conversion_buffer):
    """Removes blank lines"""
    file_buffer1 = re.sub(r"\n\n", "\n", file_conversion_buffer)
    return file_buffer1
