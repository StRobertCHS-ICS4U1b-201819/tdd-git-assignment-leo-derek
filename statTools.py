

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
            return num[len(num)//2]

        # If the number of items in the list is an even number, returns the mean of the two middle numbers
        else:
            return (num[len(num)//2 - 1] + num[len(num)//2])/2

    # Raises an error if a string is inputted or contains a string in the list
    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    # Raises an error if a number not in a list is inputted
    except AttributeError:
        raise AttributeError("A list was not provided.")


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

        # Sorts the list from least to greatest
        num.sort()

        if len(num) > 3:

            # creates a list for the first half of the original list
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

        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        else:

            num.sort()

            latter_half = num[len(num)//2 + 1:]

            if len(num) % 4 == 0:
                return (median(latter_half) + median(latter_half[:-1]))/2

            else:
                return median(latter_half)

    except TypeError:
        raise TypeError("A list was not provided or a non-number item was found in list.")

    except AttributeError:
        raise AttributeError("A list was not provided.")

