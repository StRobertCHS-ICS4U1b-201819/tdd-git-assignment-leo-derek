def mean(list):
    x = sum(list)
    y = 0
    for i in list:
        y = y + 1
    if y == 0:
        mean = 0
    else:
        mean = x / y
    return(mean)

def mode(list):
    if len(list) == 0:
        return 0
    else:
        mode = max(set(list), key=list.count)
        return mode

def variance(list):
    x = len(list)
    u = mean
