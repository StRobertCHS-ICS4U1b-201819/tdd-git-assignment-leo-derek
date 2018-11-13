"""
-------------------------------------------------------------------------------
Name:		mean.py
Purpose:
To return the mean of the list of numbers back to the user
Author:		Shat.D
Created:		07/11/2018
------------------------------------------------------------------------------
"""


def median(num: list):
    try:
        if len(num) == 0:
            raise ValueError("Illegal empty list")

        number_of_terms = len(num)

        num.sort()

        if number_of_terms % 2 == 1:
            value = num[int(number_of_terms/2)]

        else:
            value = (num[int(number_of_terms/2) - 1] + num[int(number_of_terms/2)])/2

        return value

    except AttributeError:
        raise AttributeError("A list was not provided")


"""
-------------------------------------------------------------------------------
Name:		median.py
Purpose:		
To return the median of a list of numbers back to the user
Author:		Shat.D
Created:		08/11/2018
------------------------------------------------------------------------------
"""


def range(num: list):
    try:
        if len(num) == 0:
            raise ValueError("Illegal empty list")

        num.sort()

        if len(num) >= 2:
            return num[len(num) -1] - num[0]
        elif len(num) == 1:
            return num[0]

    except TypeError:
        raise TypeError("A non-negative integer was not provided.")

    except AttributeError:
        raise AttributeError("A list was not provided")

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
        else:
            return("An error occurred")

    except AttributeError:
        raise AttributeError('A list was not provided')

    except TypeError:
        raise TypeError('A list was not provided')


"""
-------------------------------------------------------------------------------
Name:		upper_quartile.py
Purpose:		
To find the upper quartile value from a list of numbers
Author:		Shat.D
Created:		09/11/2018
------------------------------------------------------------------------------
"""


def upper_quartile(num: list):
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

    except AttributeError:
        raise AttributeError("A list was not provided")

    except TypeError:
        raise TypeError('A list was not provided')

