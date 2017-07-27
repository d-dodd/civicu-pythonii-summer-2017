#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from civicu_webapp.skeleton import fib

__author__ = "me"
__copyright__ = "me"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
