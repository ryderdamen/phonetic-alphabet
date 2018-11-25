# Phonetic Alphabet
A python package for converting characters and numbers into their phonetic equivalents.

## Installation
Installation can be done with the Python Package Index (PyPI).

```
pip install phonetic_alphabet
```

## Examples
Converting an aircraft call-sign:

```
import phonetic_alphabet as alpha

call_sign = 'CF-ABC'
response = alpha.read(call_sign)
>>> CHARLIE FOXTROT - ALPHA BRAVO CHARLIE
```

Converting digits:
```
import phonetic_alphabet as alpha

heading = 290
response = alpha.read(heading)
>>> TWO NINER ZERO
```