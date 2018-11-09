
def median(num):

    numlist = list(num)
    number_of_terms = len(numlist)

    numlist = sorted(numlist)

    if number_of_terms % 2 == 1:
        value = numlist[int(number_of_terms/2)]

    elif number_of_terms == 0:
        value = 0

    else:
        value = (numlist[int(number_of_terms/2) - 1] + numlist[int(number_of_terms/2)])/2

    return value

def range(num):

    numlist = list(num)

    numlist = sorted(numlist)

    if len(numlist) >= 2:
        return(numlist[len(numlist) -1] - numlist[0])
    elif len(numlist) == 1:
        return(numlist[0])
    else:
        return(0)

def lower_quartile(num):
        numlist = list(num)
        numlist = sorted(numlist)
        if len(numlist) > 3:
            if len(numlist) % 4 == 0:
                return(median(numlist)/2)
            else:
                first_half = numlist[:int(len(numlist)/2)]
                return(median(first_half))
        else:
            return("An error occurred")