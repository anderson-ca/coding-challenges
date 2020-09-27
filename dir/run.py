# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total = 0
    ar = [e for e in ar if ar.count(e) > 1]
    for i, e in enumerate(set(ar)):
        if ar.count(e) % 2 == 0:
            total += int(ar.count(e) / 2)
        else:
            total += int((ar.count(e) - 1) / 2)
    return total


#######################
#######################
#######################
steps = 8
path = ["U", "D", "D", "D", "U", "D", "U", "U"]


# Complete the 'countingValleys' function below.
def countingValleys(s, p):
    sl = 0
    bsl = False
    bsl_c = 0
    for i, e in enumerate(p):
        if e == "U":
            sl += 1
        elif e == "D":
            sl -= 1

        if sl < 0 and not bsl:
            bsl_c += 1
            bsl = True
        elif sl == 0 and bsl:
            bsl = False

    print(bsl_c)


countingValleys(steps, path)
