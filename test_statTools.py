import pytest
from statTools import*
def test_median_basic1():
   assert(median([3, 4, 5, 6, 7]) == 5)

def test_median_basic2():
   assert(median([3,4,2,1,5,3,7,2]) == 3)

def test_median_basic3():
   assert(median([2,3]) == 2.5)

def test_median_basic4():
   assert(median([0]) == 0)

def test_range_basic1():
    assert(range([0]) == 0)

def test_range_basic2():
    assert(range([1,2,3,4,5,6,7]) == 6)

def test_range_basic3():
    assert(range([3,5,7,3,1,7,9,4]) == 8)