import sys
from os.path import dirname, realpath
root = dirname(dirname(realpath(__file__)))
sys.path.append(root)
sys.path.append(os.path.join(root, 'phonetic_alphabet'))