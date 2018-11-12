
def median(num:list):
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




def range(num:list):
    try:
        if len(num) == 0:
            raise ValueError("Illegal empty list")

        num.sort()

        if len(num) >= 2:
            return(num[len(num) -1] - num[0])
        elif len(num) == 1:
            return(num[0])

    except TypeError:
        raise TypeError("A non-negative integer was not provided.")

    except AttributeError:
        raise AttributeError("A list was not provided")

def lower_quartile(num:list):
    try:
        if len(num) == 0:
            raise ValueError("Illegal empty list")

        num.sort()
        if len(num) > 3:
            if len(num) % 4 == 0:
                return(median(num)/2)
            else:
                first_half = num[:int(len(num)/2)]
                return(median(first_half))
        else:
            return("An error occurred")

    except AttributeError:
        raise AttributeError("A list was not provided")

def upper_quartile(num:list):
    try:
        if len(num) <= 3:
            raise ValueError("Illegal empty list or list too short")

        num.sort()
        if len(num) > 3:
            if len(num) % 4 == 0:
                return (median(num) + median(num)/2)
            else:
                latter_half = num[int(len(num)/2) + 1:]
                return (median(latter_half))

    except AttributeError:
        raise AttributeError("A list was not provided")
