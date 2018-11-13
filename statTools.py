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

def mean(list):

    try:
        return(sum(list)/len(list))
    except:
        return "An error has occurred"

'''
-----------------------------------------------------------------------------------------------------
Filename: mode.py
Purpose: returns the mode of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mode(list):

    try:
        return max(list, key=list.count)
    except AssertionError:
        raise AssertionError("must input a list")

'''
-----------------------------------------------------------------------------------------------------
Filename: variance.py
Purpose: returns the variance of a given list
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def variance(list):

    n = len(list)
    meanX = sum(list)/len(list)
    subtract_mean_from_datapoint = []
    squareOfEachDatapoint = []

    i = 0
    while i <= n-1:
        x = list[i] - meanX
        subtract_mean_from_datapoint.append(x)
        i = i + 1

    j = 0
    while j <= n-1:
        b = subtract_mean_from_datapoint[j]*subtract_mean_from_datapoint[j]
        squareOfEachDatapoint.append(b)
        j = j + 1

    coolX = sum(squareOfEachDatapoint)
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

def standard_deviation(list):

    n = len(list)
    meanX = sum(list) / len(list)
    subtract_mean_from_datapoint = []
    squareOfEachDatapoint = []

    i = 0
    while i <= n - 1:
        x = list[i] - meanX
        subtract_mean_from_datapoint.append(x)
        i = i + 1

    j = 0
    while j <= n - 1:
        b = subtract_mean_from_datapoint[j] * subtract_mean_from_datapoint[j]
        squareOfEachDatapoint.append(b)
        j = j + 1

    coolX = sum(squareOfEachDatapoint)
    varNum = (coolX / (n - 1))

    return(float("%0.2f" % (math.sqrt(varNum))))
