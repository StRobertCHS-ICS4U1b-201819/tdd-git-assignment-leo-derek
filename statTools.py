
def median(num):
    value = 0

    numlist = list(num)
    number_of_terms = int(len(numlist))
    print(number_of_terms)

    # bubble sort the list
    numlist = sorted(numlist)

    if number_of_terms % 2 == 1:
        value = numlist[int(number_of_terms/2)]
    elif number_of_terms == 0:
        value = 0
    else:
        value = (numlist[int(number_of_terms/2) - 1] + numlist[int(number_of_terms/2)])/2
    return value