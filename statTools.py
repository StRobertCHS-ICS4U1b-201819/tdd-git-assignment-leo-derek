import math

# ----------------------------------------------------------------------------------------------------- #
# Filename: statTools.py                                                                                #
# Purpose: functions that find statistics: mean, mode, variance, standard deviation                     #
# Author: L, Xiao                                                                                       #
# Created: 31/10/2018                                                                                   #
# ----------------------------------------------------------------------------------------------------- #


def mean(data_set):

    """Given a list of numbers, return the mean of that list
    :param data_set: list of numbers
    :return: mean of a list of numbers
    """

    try:

        # Check to see if list has more than one number
        if len(data_set) < 1:
            return None
        else:

            # Adds all the numbers in the list and then divides that by the amount of numbers in the list and
            # rounds to two decimals to avoid python rounding errors
            return round(sum(data_set)/len(data_set), 2)

        # Raises type error if a list of integers was not found
    except TypeError:
        raise TypeError("Error: please input a list of integers")


def mode(data_set):

    """Given a list of numbers, return the mode of that list
    :param data_set: list of numbers
    :return: the mode of that list of numbers
    """

    try:
        # Check to see if the list has any numbers

        int_list = [int(i) for i in data_set]

        if len(int_list) < 1:
            return None

        # Counts the number of times each value appears in the list and returns the most common number
        else:
            most_common_number = max(set(int_list), key=int_list.count)

            return most_common_number

    # Raises value error if a list of strings were found
    except ValueError:
        raise ValueError("Error: please input a list of integers")


def variance(data_set):

    """Given a list of numbers, return the variance of that list
    :param data_set: list of numbers
    :return: the variance of that list of numbers
    """

    # Check to see if the list has 2 or more numbers since you require more than 1 number to find variance
    if len(data_set) <= 1:
        return None

    else:
        try:

            # Initialize the variables for easy access later
            n = len(data_set)
            mean_of_data = sum(data_set)/len(data_set)

            # Initialize lists to use later
            subtract_mean_from_data = []
            square_of_each_point = []

            # Subtracts all numbers in the list by the mean and stores that in a new list
            i = 0
            while i <= n-1:
                x = data_set[i] - mean_of_data
                subtract_mean_from_data.append(x)
                i = i + 1

            # Squares all the numbers in the new list and stores those numbers in another new list
            j = 0
            while j <= n-1:
                b = subtract_mean_from_data[j]*subtract_mean_from_data[j]
                square_of_each_point.append(b)
                j = j + 1

            # Divide the sum of the second new list by the length of the initial list to calculate variance
            variance_of_data = (sum(square_of_each_point) / (n - 1))

            return variance_of_data

        # Raises type error if a list of integers was not found
        except TypeError:
            raise TypeError("Error: please input a list of integers")


def standard_deviation(data_set):

    """Given a list of numbers, return the standard deviation of that list
    :param data_set: list of numbers
    :return: the standard deviation of that list of numbers
    """

    # Calculates the variance
    if len(data_set) <= 1:
        return None
    else:
        try:
            n = len(data_set)
            mean_of_data = sum(data_set) / len(data_set)
            subtract_mean_from_data = []
            square_of_each_point = []
    
            i = 0
            while i <= n - 1:
                x = data_set[i] - mean_of_data
                subtract_mean_from_data.append(x)
                i = i + 1
    
            j = 0
            while j <= n - 1:
                b = subtract_mean_from_data[j] * subtract_mean_from_data[j]
                square_of_each_point.append(b)
                j = j + 1
            
            variance_of_data = (sum(square_of_each_point) / (n - 1))
            
            # Square roots the variance to calculate standard deviation
            return float("%0.2f" % (math.sqrt(variance_of_data)))

        # Raises type error if a list of integers was not found
        except TypeError:
            raise TypeError("Error: please input a list of integers")
