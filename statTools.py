import math

# ----------------------------------------------------------------------------------------------------- #
# Filename: statTools.py                                                                                #
# Purpose: functions that find statistics: mean, mode, variance, standard deviation                     #
# Author: L. Xiao                                                                                       #
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
            return round(sum(data_set) / len(data_set), 2)

    # Raises type error if a list of integers was not found
    except TypeError:
        raise TypeError("Error: please input a list of integers")


def median(num: list):
    """Finds the median of the list
    :param num: the list of numbers
    :return: int or float The number or mean of the numbers that appear in the middle of the list after sorted least
    to greatest
    """

    try:

        # Raises an error if the list is empty
        if len(num) < 1:
            raise ValueError("Illegal empty list or list too short")

        # Sorts the list from least to greatest
        num.sort()

        # If the number of items in the list is an odd number, returns the number in the middle
        if len(num) % 2 == 1:

            # multiplication and division are there to ensure code will not work with strings
            return num[len(num)//2]/2*2

        # If the number of items in the list is an even number, returns the mean of the two middle numbers
        else:
            return (num[len(num)//2 - 1] + num[len(num)//2])/2

    # Raises an error if a string is inputted or contains a string in the list
    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    # Raises an error if a number not in a list is inputted
    except AttributeError:
        raise AttributeError("A list was not provided.")


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


def range(num: list):
    """Finds the range of the list
      :param num: the list of numbers
      :return: int or float The difference between the greatest and least value in the list
      """

    try:

        # Raises an error if the list contains less than 2 objects
        if len(num) < 2:
            raise ValueError('Illegal empty list or list too short')

        # Sorts the list from least to greatest
        num.sort()

        # If the number of objects in the list is greater than 1, returns the difference of the last number in the list
        # and the first number in the list
        if len(num) >= 2:
            return num[len(num) - 1] - num[0]

        # If there is only one object in the list, returns that value
        elif len(num) == 1:
            return num[0]

    # Raises an error if a string is inputted or contains a string in the list
    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    # Raises an error if a number not in a list is inputted
    except AttributeError:
        raise AttributeError("A list was not provided.")


def lower_quartile(num: list):
    """Finds the lower quartile of the list
      :param num: the list of numbers
      :return: int or float The number or mean of the numbers that appear in the middle of the first half of the list
      after sorted least to greatest
      """

    try:

        # Raises an error if the list contains less than 4 objects
        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        else:

            # Sorts the list from least to greatest
            num.sort()

            # Creates a list for the first half of the original list
            first_half = num[:len(num)//2]

            # Returns the median of the first half of the list
            if len(num) % 4 == 0:
                return (median(first_half[:-1]) + median(first_half))/2

            else:
                return median(first_half)

    # Raises an error when a list is not provided or a non-number item is found in the list
    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    # Raises an error when a list is not provided
    except AttributeError:
        raise AttributeError('A list was not provided.')


def upper_quartile(num: list):
    """Finds the upper quartile of the list
      :param num: the list of numbers
      :return: int or float The number or mean of the numbers that appear in the middle of the second half of the list
      after sorted least to greatest
      """

    try:

        # Raises an error if the list contains less than 4 objects
        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        else:

            # Sorts the list from least to greatest
            num.sort()

            # Creates a ;ost fpr the latter half of the original list
            latter_half = num[len(num)//2 + 1:]

            # Returns the median of the latter half
            if len(num) % 4 == 0:
                return (median(latter_half) + median(latter_half[:-1]))/2

            else:
                return median(latter_half)

    # Raises an error when a list is not provided or a non-number item is found in the list
    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    # Raises an error when a list is not provided
    except AttributeError:
        raise AttributeError("A list was not provided.")





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
            mean_of_data = sum(data_set) / len(data_set)

            # Initialize lists to use later
            subtract_mean_from_data = []
            square_of_each_point = []

            # Subtracts all numbers in the list by the mean and stores that in a new list
            i = 0
            while i <= n - 1:
                x = data_set[i] - mean_of_data
                subtract_mean_from_data.append(x)
                i = i + 1

            # Squares all the numbers in the new list and stores those numbers in another new list
            j = 0
            while j <= n - 1:
                b = subtract_mean_from_data[j] * subtract_mean_from_data[j]
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

