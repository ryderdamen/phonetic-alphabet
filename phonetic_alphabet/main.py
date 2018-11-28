""" Phonetic Alphabet - Main Logic """

from . import helpers


class NonSupportedTextException(Exception):
    """ Raised when non-supported text is passed to the phonetic alphabet methods """
    pass


def _process_replacements(input_text):
    """ Handles the processing of replacements """
    original_input = list(input_text)  # Immutable
    replaced = list(input_text)
    for index, char in enumerate(original_input):
        if char.isalpha() or char.isdigit():
            replacement = helpers.get_character(char)
            if replacement:
                replaced[index] = ' ' + replacement + ' '
    return helpers.remove_excess_spaces(''.join(replaced))


def read(text):
    """Reads input characters back as phonetic characters
    
    Arguments:
        text {str} -- The input text to convert to phonetics
    """
    text = str(text)
    if not helpers.contains_only_phonetic_chars(text):
        raise NonSupportedTextException()
    return _process_replacements(text)
