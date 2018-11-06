
def median(num):
    value = 0

    numlist = list(num)
    number_of_terms = int(len(numlist))
    print(number_of_terms)

    # bubble sort the list
    has_swapped = True
    while has_swapped:
        has_swapped = False

        for i in range(number_of_terms - 1):
            if numlist[i + 1] < numlist[i]:
                numlist[i + 1], numlist[i] = numlist[i], numlist[i + 1]
                has_swapped = True
            i += 1

    if number_of_terms % 2 == 1:
        value = numlist[int(number_ofgit_terms/2)]
    elif number_of_terms == 0:
        value = 0
    else:
        value = (numlist[int(number_of_terms/2) - 1] + numlist[int(number_of_terms/2)])/2
    return value