""" Main unit tests for Phonetic Alphabet package """

from phonetic_alphabet import read


def test_read_can_convert_alpha_chars():
    result = read('abcd ABCD')
    expected = 'ALFA BRAVO CHARLIE DELTA ALFA BRAVO CHARLIE DELTA'
    assert result == expected


def test_read_can_convert_digit_chars():
    result = read('67890')
    expected = 'SIX SEVEN EIGHT NINER ZERO'
    assert result == expected


def test_read_can_convert_digit_and_alpha():
    result = read('6 a 7 b 8 c 9 d 0')
    expected = 'SIX ALFA SEVEN BRAVO EIGHT CHARLIE NINER DELTA ZERO'
    assert result == expected


def test_read_can_handle_simple_punctuation():
    result = read('6. a 7 b 8 c 9 d 0')
    expected = 'SIX . ALFA SEVEN BRAVO EIGHT CHARLIE NINER DELTA ZERO'
    assert result == expected


def test_read_can_handle_aircraft_call_signs():
    call_sign = 'CF-ABC'
    result = read(call_sign)
    expected = 'CHARLIE FOXTROT - ALFA BRAVO CHARLIE'
    assert result == expected


def test_read_can_handle_int_types():
    assert read(290) == "TWO NINER ZERO"
