# return masked string
def maskify(cc):
    if len(list(cc)) <= 4:
        return cc
    else:
        length = len(list(cc)) - 1
        listcc = list(cc)
        hashtags = "#" * (length - 3)
        lastfour = str(listcc[length-3] + listcc[length-2]) + listcc[length-1] + listcc[length]
        masked = hashtags + lastfour
        return masked