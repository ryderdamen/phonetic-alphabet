""" Helper methods for Phonetic Alphabet package """

import re
from .data.icao_alphabet import icao_alphabet
from .data.numbers import numbers


def extra_supported_chars():
    """ Returns extra supported chars besides phonetics """
    return [
        '.',
        ',',
        ' ',
        ';',
        ':',
        '?',
        '-',
    ]


def contains_only_phonetic_chars(text):
    """ Determines if text contains only phonetic-capable characters """
    pattern = '[^A-Za-z0-9 {}]'.format(''.join(extra_supported_chars()))
    return not bool(re.compile(pattern).search(text))


def get_alpha(character):
    """ Gets the phonetic version of an alpha character """
    if character.upper() in icao_alphabet:
        return icao_alphabet[character.upper()]


def get_number(character):
    """ Gets the phonetic version of a digit """
    if int(character) in numbers:
        return numbers[int(character)]


def get_character(character):
    """ Returns the phonetic version of a character (mapping method) """
    if character.isalpha():
        return get_alpha(character)
    elif character.isdigit():
        return get_number(character)
    return None


def remove_excess_spaces(text):
    """ Removes duplicate spaces from a string """
    return ' '.join(text.split())
