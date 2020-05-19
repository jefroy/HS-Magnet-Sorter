# -*- coding: utf-8 -*-

import pytest
from hs_magnet_sorter.skeleton import fib

__author__ = "Ajay"
__copyright__ = "Ajay"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
