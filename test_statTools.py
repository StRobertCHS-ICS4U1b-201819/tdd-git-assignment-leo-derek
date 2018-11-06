import pytest
from statTools import *

def test_mean():
    mean_list = [50, 100, 75, 25]
    x = sum(mean_list)
    y = 0
    for i in mean_list:
        y = y + 1
    mean = x/y
    print(mean)