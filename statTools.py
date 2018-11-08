def mean(list):
    if len(list) > 0:
        return(sum(list)/len(list))
    else:
        return(0)

def mode(list):
    if len(list) == 0:
        return 0
    else:
        mode = max(set(list), key=list.count)
        return mode

