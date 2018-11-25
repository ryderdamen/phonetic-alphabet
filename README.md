# Phonetic Alphabet
A Python package for converting characters and digits to phonetic alphabet equivalents.

## Installation
Installation can be done with the Python Package Index (PyPI).

```bash
pip install phonetic_alphabet
```

## Examples
Converting an aircraft call-sign:

```python
import phonetic_alphabet as alpha

call_sign = 'CF-ABC'
response = alpha.read(call_sign)
>>> CHARLIE FOXTROT - ALPHA BRAVO CHARLIE
```

Converting digits:
```python
import phonetic_alphabet as alpha

heading = 290
response = alpha.read(heading)
>>> TWO NINER ZERO
```