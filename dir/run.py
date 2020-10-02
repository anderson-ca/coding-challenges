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


path = ["U", "D", "D", "D", "U", "D", "U", "U"]


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


array = [3, 5, -4, 8, 11, 1, -1, 6]

target = 10


# O(n^2) time | O(1) space
def twoNumberSum0(a, t):
    res = list()
    for i, e in enumerate(a):
        if len(res) == 2:
            break
        for q in range(len(a)):
            if e + a[q] == t and i != q:
                res.append(e)
                res.append(a[q])
                break

    return res


# O(n) time | O(n) space
def twoNumberSum1(a, t):
    nums = {}
    for i in a:
        x = t - i
        if x in nums:
            return [x, i]
        else:
            nums[num] = "not it"
    return []


#######################
#######################
#######################
a = [5, 1, 22, 25, 6, -1, 8, 10]
b = [1, 6, -1, 10]
c = ['A', "B"]

fail_a = [5, 1, 22, 25, 6, -1, 8, 10]
fail_b = [5, 1, 22, 25, 6, -1, 8, 10, 10]


# definition - the sub-sequence list B should be derived
# from sequence A by deleting some or none elements without
# changing the order of the remaining elements in list A.
# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
    idA = 0
    idB = 0

    while idA < len(array) and idB < len(sequence):
        if array[idA] == sequence[idB]:
            idB += 1
        idA += 1

    return len(sequence) == idB
