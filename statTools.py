
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
        if len(numlist) > 2:
            if len(numlist) % 4 != 0:
                return(numlist[int(len(numlist)/4)])
            else:
                return((numlist[int(len(numlist)/4)] + numlist[int(len(numlist)/4)-1])/2)

        else:
            return(numlist[0])