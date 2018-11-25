""" Phonetic Alphabet - Entry point for package """

import sys
from os.path import dirname, realpath
root = dirname(dirname(realpath(__file__)))
sys.path.append(root)

from main import read
