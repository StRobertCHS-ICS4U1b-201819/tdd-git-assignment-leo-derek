import pytest
from statTools import*
def test_median_basic1():
   assert(median([3, 4, 5, 6, 7]) == 5)

def test_median_basic2():
   assert(median([3, 4, 2, 1, 5, 3, 7, 2]) == 3)

def test_median_basic3():
   assert(median([2, 3]) == 2.5)

def test_median_basic4():
   assert(median([0]) == 0)

def test_median_basic5():
    assert(median("") == 0)

def test_median_basic6():
    assert(median([0.3, 0.4, 0.2, 0.1, 0.5, 0.3, 0.7, 0.2]) == 0.3)


def test_range_basic1():
    assert(range([0]) == 0)

def test_range_basic2():
    assert(range([1, 2, 3, 4, 5, 6, 7]) == 6)

def test_range_basic3():
    assert(range([3, 5, 7, 3, 1, 7, 9, 4]) == 8)

def test_range_basic4():
    assert(range([0, -2, 1, -5, 3, -9, 10]) == 19)

def test_range_basic5():
    assert(range("") == 0)

def test_range_basic6():
    assert(range([0.3, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4]) == 0.8)


def test_lower_quartile_basic1():
    assert(lower_quartile([3, 4, 5, 6, 7]) == 3.5)

def test_lower_quartile_basic2():
    assert(lower_quartile([3, 4, 6, 1, 5, 8, 7, 2]) == 2.25)
    #1,2,3,4,5,6,7,8

def test_lower_quartile_basic3():
    assert(lower_quartile([2, 3]) == "An error occurred")

def test_lower_quartile_basic4():
    assert(lower_quartile([0]) == "An error occurred")

def test_lower_quartile_basic5():
    assert (lower_quartile([0, -2, 1, -5, 3, -9, 10]) == -5)
    #-9,-5,-2,0,1,3,10

def test_lower_quartile_basic6():
    assert(lower_quartile([0.2, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4, 1]) == 0.25)
    #0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.7, 0.9, 1

def test_upper_quartile_basic1():
    assert(upper_quartile([3, 4, 5, 6, 7]) == 6.5)

def test_upper_quartile_basic2():
    assert(upper_quartile([3, 4, 6, 1, 5, 8, 7, 2]) == 6.75)
    #1,2,3,4,5,6,7,8

def test_upper_quartile_basic3():
    assert(upper_quartile([2, 3]) == "An error occurred")

def test_upper_quartile_basic4():
    assert(upper_quartile([0]) == "An error occurred")

def test_upper_quartile_basic5():
    assert(upper_quartile([0, -2, 1, -5, 3, -9, 10]) == 3)
    #-9,-5,-2,0,1,3,10

def test_upper_quartile_basic6():
    assert(upper_quartile([0.2, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4, 1]) == 0.8)
    #0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.7, 0.9, 1