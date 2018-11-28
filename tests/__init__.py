import sys
from os.path import dirname, realpath, join
root = dirname(dirname(realpath(__file__)))
sys.path.append(root)
sys.path.append(join(root, 'phonetic_alphabet'))