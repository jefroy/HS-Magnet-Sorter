from hs_magnet_sorter.magnet_helper import *
import os

sep = "=" * 60
print(sep)
DIR1 = os.path.dirname(
    "data"
)
DATA_DIR = os.path.abspath(
    os.path.dirname("data")
)
data_path = '../data'
# print(DATA_DIR)
print(DIR1)
print(read_file('links.txt', data_path))
print(read_file('empty.txt', data_path))
