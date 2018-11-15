import math
'''
-----------------------------------------------------------------------------------------------------
Filename: statTools.py
Purpose: functions that find statistics: mean, mode, variance, standard deviation
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''
'''
-----------------------------------------------------------------------------------------------------
Filename: mean.py
Purpose: when given a list, returns the mean of the list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mean(data_set):
    """Given a list of numbers, return the mean of that list
    :param data_set: list of numbers
    :return: mean of a list of numbers
    """
    try:
        if len(data_set) < 1:
            return None
        else:
            return sum(data_set)/len(data_set)
    except TypeError:
        return "Error: please input a list of integers"

'''
-----------------------------------------------------------------------------------------------------
Filename: mode.py
Purpose: returns a list of mode of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mode(data_set):
    '''Given a list of numbers, return the mode of that list
    :param data_set: list of numbers
    :return: the mode of that list of numbers
    '''

    # Check to see if the list has any numbers

    int_list = [int(i) for i in data_set]

    if len(int_list) < 1:
        return None

    # Counts the number of times each value appears in the list and returns the most common number
    else:
        try:
            mode = max(set(int_list), key=int_list.count)
            return mode
        except ValueError:
            return "Error: please input a list of integers"

'''
-----------------------------------------------------------------------------------------------------
Filename: variance.py
Purpose: returns the variance of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def variance(data_set):
    """Given a list of numbers, return the variance of that list
    :param data_set: list of numbers
    :return: the variance of that list of numbers
    """

    n = len(data_set)
    meanX = sum(data_set)/len(data_set)
    subtract_mean_from_datapoint = []
    square_of_each_point = []

    i = 0
    while i <= n-1:
        x = data_set[i] - meanX
        subtract_mean_from_datapoint.append(x)
        i = i + 1

    j = 0
    while j <= n-1:
        b = subtract_mean_from_datapoint[j]*subtract_mean_from_datapoint[j]
        square_of_each_point.append(b)
        j = j + 1

    coolX = sum(square_of_each_point)
    varNum = (coolX/(n-1))
    return(varNum)

'''
-----------------------------------------------------------------------------------------------------
Filename: standard_deviation.py
Purpose: returns the standard deviation of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def standard_deviation(data_set):
    """Given a list of numbers, return the standard deviation of that list
    :param data_set: list of numbers
    :return: the standard deviation of that list of numbers
    """

    n = len(data_set)
    meanX = sum(data_set) / len(data_set)
    subtract_mean_from_datapoint = []
    square_of_each_point = []

    i = 0
    while i <= n - 1:
        x = data_set[i] - meanX
        subtract_mean_from_datapoint.append(x)
        i = i + 1

    j = 0
    while j <= n - 1:
        b = subtract_mean_from_datapoint[j] * subtract_mean_from_datapoint[j]
        square_of_each_point.append(b)
        j = j + 1

    coolX = sum(square_of_each_point)
    varNum = (coolX / (n - 1))

    return(float("%0.2f" % (math.sqrt(varNum))))