# -*- coding: utf-8 -*-

import pytest
from hs_magnet_sorter.magnet_helper import *


__author__ = "Ajay"
__copyright__ = "Ajay"
__license__ = "mit"


def test_read_file():
    lines1 = read_file('links.txt')
    # lines2 = read_file('??.txt')
    assert lines1, "pass"
    # assert lines2, "fail"


def test_process_array():
    test_arr = [1, 2, 4, 5]
    arr1 = process_array(test_arr)
    print(arr1)
    assert len(arr1) == len(test_arr), "pass"