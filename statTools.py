def mean(list):
    try:
        return(sum(list)/len(list))
    except:
        return("An error has occurred")

def mode(list):
    if len(list) == 0:
        return 0
    else:
        mode = max(set(list), key=list.count)
        return mode

def variance(list):
    n = len(list)
    meanX = sum(list)/len(list)
    subtractMeanFromDatapoint = []
    squareOfEachDatapoint = []

    i = 0
    while i < n:
        x = list[i] - meanX
        subtractMeanFromDatapoint.append(x)
        i = i + 1

    j = 0
    while j < n:
        b = subtractMeanFromDatapoint[j]*subtractMeanFromDatapoint[j]
        squareOfEachDatapoint.append(b)
        j = j + 1

    coolX = sum(squareOfEachDatapoint)
    varNum = float(coolX/n-1)
    return(varNum)