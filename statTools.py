import math
'''
-----------------------------------------------------------------------------------------------------
Filename: statTools.py
Purpose: functions that find statistics: mean, mode, variance, standard deviation
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------
Filename: mean.py
Purpose: when given a list, returns the mean of the list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mean(data_set):

    try:
        return(sum(data_set)/len(data_set))
    except:
        return "An error has occurred"

'''
-----------------------------------------------------------------------------------------------------
Filename: mode.py
Purpose: returns a list of mode of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mode(data_set):
    # raise error if input is not a list
    if type(data_set) != list:
        raise TypeError("input must be a list")

    # return none if empty list
    if len(data_set) == 0:
        return None

    count = {}
    highest = 0
    # adds every item occurrence to a dict mapping to the number of times the item appears
    # keep track of greatest occurrence

    for item in data_set:
        if item in count:
            count[item] += 1

        else:
            count[item] = 1

        if count[item] > highest:
            highest = count[item]

    # finds all values that have the same number of occurrences as the greatest number of occurrences
    out = [unique for unique in count if count[unique] == highest]
    # returns single value if only 1 mode- list of values if multiple
    return(out)

'''
-----------------------------------------------------------------------------------------------------
Filename: variance.py
Purpose: returns the variance of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def variance(data_set):

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
