

def median(num: list):
    """Finds the median of the list
    :param num: the list of numbers
    :return: int or float The number or mean of the numbers that appear in the middle of the list after sorted least
    to greatest
    """

    try:
        if len(num) < 1:
            raise ValueError("Illegal empty list or list too short")

        number_of_terms = len(num)

        num.sort()

        if number_of_terms % 2 == 1:
            value = num[int(number_of_terms/2)]

        else:
            value = (num[int(number_of_terms/2) - 1] + num[int(number_of_terms/2)])/2

        return value

    except TypeError:
        raise TypeError("A list was not provided or no numbers were found in list.")

    except AttributeError:
        raise AttributeError("A list was not provided.")


def range(num: list):
    """Finds the range of the list
      :param num: the list of numbers
      :return: int or float The difference between the greatest and least value in the list
      """

    try:
        if len(num) < 2:
            raise ValueError('Illegal empty list or list too short')

        num.sort()

        if len(num) >= 2:
            return num[len(num) -1] - num[0]

        elif len(num) == 1:
            return num[0]

    except TypeError:
        raise TypeError("A list was not provided or no numbers were found in list.")

    except AttributeError:
        raise AttributeError("A list was not provided.")


"""
-------------------------------------------------------------------------------
Name:		lower_quartile.py
Purpose:		
To find the lower quartile value from a list of numbers
Author:		Shat.D
Created:		09/11/2018
------------------------------------------------------------------------------
"""


def lower_quartile(num: list):
    """Finds the lower quartile of the list
      :param num: the list of numbers
      :return: int or float The number or mean of the numbers that appear in the middle of the first half of the list
      after sorted least to greatest
      """

    try:

        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        num.sort()

        if len(num) > 3:

            if len(num) % 4 == 0:
                return median(num)/2

            else:
                first_half = num[:int(len(num)/2)]
                return median(first_half)

    except TypeError:
        raise TypeError("A list was not provided or no numbers were found in list.")

    except AttributeError:
        raise AttributeError('A list was not provided.')


def upper_quartile(num: list):
    """Finds the upper quartile of the list
      :param num: the list of numbers
      :return: int or float The number or mean of the numbers that appear in the middle of the second half of the list
      after sorted least to greatest
      """

    try:
        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        num.sort()

        if len(num) > 3:

            if len(num) % 4 == 0:
                return median(num) + median(num)/2

            else:
                latter_half = num[int(len(num)/2) + 1:]
                return median(latter_half)

    except TypeError:
        raise TypeError("A list was not provided or no numbers were found in list.")

    except AttributeError:
        raise AttributeError("A list was not provided.")

