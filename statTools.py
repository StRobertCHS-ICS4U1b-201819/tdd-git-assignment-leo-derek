
def median(num):
    value = 0

    numlist = list(num)

    number_of_terms = len(numlist)


    # bubble sort the list
    has_swapped = True
    while has_swapped:
        has_swapped = False

        for i in range(n - 1):
            if numlist[i + 1] < numlist[i]:
                numlist[i + 1], numlist[i] = numlist[i], numlist[i + 1]
                has_swapped = True
          i += 1

        if number_of_terms % 2 == 0:
            return numlist[number_of_terms/2]