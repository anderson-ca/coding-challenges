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
