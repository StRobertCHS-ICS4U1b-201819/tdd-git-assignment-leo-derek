import pytest
from statTools import *
def test_mean_basic1():
    assert(mean([10]) == 10)

def test_mean_basic2():
    assert(mean([10, 20, 30]) == 20)

def test_mean_basic3():
    assert(mean([0.1, 0.2, 0.3]) == 0.20000000000000004)

def test_mean_basic4():
    assert(mean([0]) == 0)

def test_mean_basic5():
    assert(mean([]) == None)

def test_mean_type_error():
    assert(mean(["a b c"]) == "Error: please input a list of integers")

def test_mode_basic1():
    assert(mode([1, 2, 3, 3, 3]) == 3)

def test_mode_basic2():
    assert(mode([1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 3)

def test_mode_basic3():
    assert(mode([1, 2, 2, 3, 3, 3, 3, 3]) == 3)

def test_mode_basic4():
    assert(mode([1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 2)

'''
def test_mode_basic5():
    assert(mode("hello") == "l")
'''
def test_variance_basic1():
    assert(variance([17, 15, 23, 7, 9, 13]) == 33.2)

def test_variance_basic2():
    assert(variance([1, 2, 3, 4, 5, 6]) == 3.5)

def test_variance_basic3():
    assert(variance([10, 20, 30]) == 100)

def test_variance_basic4():
    assert(variance([1, 10, 10, 20, 46, 240]) == 8499.1)

def test_standard_deviation_basic1():
    assert(standard_deviation([10, 20, 30]) == 10)

def test_standard_deviation_basic2():
    assert(standard_deviation([1, 10, 10, 20, 46, 240]) == 92.19)

def test_standard_deviation_basic3():
    assert(standard_deviation([1, 2, 3, 4, 5, 6]) == 1.87)

def test_standard_deviation_basic4():
    assert(standard_deviation([0, 1, 1, 2, 2, 3]) == 1.05)