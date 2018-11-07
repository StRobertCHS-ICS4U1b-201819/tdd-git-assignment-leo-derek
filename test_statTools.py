import pytest
from statTools import *
def test_mean_basic1():
    assert(mean([10]) == 10)

def test_mean_basic2():
    assert(mean([10, 20, 30]) == 20)

def test_mean_basic3():
    assert(mean([]) == 0)

def test_mean_basic4():
    assert(mean([0.1, 0.2, 0.3]) == 0.20000000000000004)

def test_mode_basic1():
    assert(mode([0]) == 0)

def test_mode_basic2():
    assert(mode([0, 1, 1, 2, 3]) == 1)

def test_mode_basic3():
    assert(mode([0.1, 0.1, 0.3]) == 0.1)

def test_mode_basic4():
    assert(mode([]) == 0)