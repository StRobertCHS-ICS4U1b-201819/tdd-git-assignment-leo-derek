import pytest
from statTools import*


def test_median_basic1():
   assert(median([3, 4, 5, 6, 7]) == 5)


def test_median_basic2():
   assert(median([3, 4, 2, 1, 5, 3, 7, 2]) == 3)


def test_median_basic3():
   assert(median([2, 3]) == 2.5)


def test_median_basic4():
    assert(median([0.3, 0.4, 0.2, 0.1, 0.5, 0.3, 0.7, 0.2]) == 0.3)


def test_median_value_error():
    with pytest.raises(ValueError) as errmsg:
        median([])
    assert ('Illegal empty list or list too short' == str(errmsg.value))


def test_median_type_error1():
    with pytest.raises(TypeError) as errmsg:
        median(["hello", "hi"])
    assert ('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_median_type_error2():
    with pytest.raises(TypeError) as errmsg:
        median(0)
    assert('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_median_attribute_error():
    with pytest.raises(AttributeError) as errmsg:
        median("hello")
    assert ('A list was not provided.' == str(errmsg.value))


def test_range_basic1():
    assert(range([1, 2, 3, 4, 5, 6, 7]) == 6)


def test_range_basic2():
    assert(range([3, 5, 7, 3, 1, 7, 9, 4]) == 8)


def test_range_basic3():
    assert(range([0, -2, 1, -5, 3, -9, 10]) == 19)


def test_range_basic4():
    assert(range([0.3, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4]) == 0.8)


def test_range_value_error():
    with pytest.raises(ValueError) as errmsg:
        range([])
    assert ('Illegal empty list or list too short' == str(errmsg.value))


def test_range_attribute_error():
    with pytest.raises(AttributeError) as errmsg:
        range("hello")
    assert ('A list was not provided.' == str(errmsg.value))

def test_range_type_error1():
    with pytest.raises(TypeError) as errmsg:
        range(["hello", "hi"])
    assert ('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_range_type_error2():
    with pytest.raises(TypeError) as errmsg:
        range(0)
    assert('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_lower_quartile_basic1():
    assert(lower_quartile([3, 4, 5, 6, 7]) == 3.5)


def test_lower_quartile_basic2():
    assert(lower_quartile([3, 4, 6, 1, 5, 8, 7, 2]) == 2.25)


def test_lower_quartile_basic3():
    assert (lower_quartile([0, -2, 1, -5, 3, -9, 10]) == -5)


def test_lower_quartile_basic4():
    assert(lower_quartile([0.2, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4, 1]) == 0.25)


def test_lower_quartile_value_error():
    with pytest.raises(ValueError) as errmsg:
        lower_quartile([])
    assert('Illegal empty list or list too short' == str(errmsg.value))


def test_lower_quartile_type_error1():
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(["hello", "hi", "hello there", "bye"])
    assert ('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_lower_quartile_type_error2():
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(0)
    assert('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_lower_quartile_attribute_error():
    with pytest.raises(AttributeError) as errmsg:
        lower_quartile("hello")
    assert ('A list was not provided.' == str(errmsg.value))


def test_upper_quartile_basic1():
    assert(upper_quartile([3, 4, 5, 6, 7]) == 6.5)


def test_upper_quartile_basic2():
    assert(upper_quartile([3, 4, 6, 1, 5, 8, 7, 2]) == 6.75)


def test_upper_quartile_basic3():
    assert(upper_quartile([0, -2, 1, -5, 3, -9, 10]) == 3)


def test_upper_quartile_basic4():
    assert(upper_quartile([0.2, 0.5, 0.7, 0.3, 0.1, 0.7, 0.9, 0.4, 1]) == 0.8)


def test_upper_quartile_value_error():
    with pytest.raises(ValueError) as errmsg:
        upper_quartile([])
    assert('Illegal empty list or list too short' == str(errmsg.value))


def test_upper_quartile_attribute_error():
    with pytest.raises(AttributeError) as errmsg:
        upper_quartile("hello")
    assert ('A list was not provided.' == str(errmsg.value))

def test_upper_quartile_type_error1():
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(["hello", "hi", "hello there", "bye"])
    assert ('A list was not provided or no numbers were found in list.' == str(errmsg.value))


def test_upper_quartile_type_error2():
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(0)
    assert('A list was not provided or no numbers were found in list.' == str(errmsg.value))
