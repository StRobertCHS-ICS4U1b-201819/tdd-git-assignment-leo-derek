import math
'''
-----------------------------------------------------------------------------------------------------
Filename: statTools.py
Purpose: functions that find statistics: mean, mode, variance, standard deviation
Author: L, Xiao
Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
'''

def mean(list):

    try:
        return(sum(list)/len(list))
    except:
        return("An error has occurred")

def mode(list):

    try:
        return max(list, key=list.count)
    except AssertionError:
        raise AssertionError("must input a list")

def variance(list):

    n = len(list)
    meanX = sum(list)/len(list)
    subtractMeanFromDatapoint = []
    squareOfEachDatapoint = []

    i = 0
    while i <= n-1:
        x = list[i] - meanX
        subtractMeanFromDatapoint.append(x)
        i = i + 1

    j = 0
    while j <= n-1:
        b = subtractMeanFromDatapoint[j]*subtractMeanFromDatapoint[j]
        squareOfEachDatapoint.append(b)
        j = j + 1

    coolX = sum(squareOfEachDatapoint)
    varNum = (coolX/(n-1))
    return(varNum)

def standard_deviation(list):

    n = len(list)
    meanX = sum(list) / len(list)
    subtractMeanFromDatapoint = []
    squareOfEachDatapoint = []

    i = 0
    while i <= n - 1:
        x = list[i] - meanX
        subtractMeanFromDatapoint.append(x)
        i = i + 1

    j = 0
    while j <= n - 1:
        b = subtractMeanFromDatapoint[j] * subtractMeanFromDatapoint[j]
        squareOfEachDatapoint.append(b)
        j = j + 1

    coolX = sum(squareOfEachDatapoint)
    varNum = (coolX / (n - 1))

    return(float("%0.2f" % (math.sqrt(varNum))))
