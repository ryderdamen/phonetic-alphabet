""" Tests for the helpers of the phonetic alphabet """

from phonetic_alphabet import helpers


def test_contains_only_phonetic_chars_will_recognize_phonetics():
    """ Tests the contains_only_phonetic_chars() method recognizes real phonetic chars """
    example_text = "The quick brown fox jumps over the lazy dog 1234567890"
    assert helpers.contains_only_phonetic_chars(example_text) == True


def test_contains_only_phonetic_chars_will_recognize_non_phonetics():
    """ Tests the contains_only_phonetic_chars() method recognizes real phonetic chars """
    example_text = "The quick brown fox jumps over the lazy dog. 1234567890\n"
    assert helpers.contains_only_phonetic_chars(example_text) == False
