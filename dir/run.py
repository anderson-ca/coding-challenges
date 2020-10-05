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


def super_size(n):
    # your code here
    q = []
    for i in str(n):
        q.append(i)

    return int(''.join(q.sort(reverse=True)))


def logical_calc(array, op):
    state = None
    operation = None

    if op == "AND":
        for i in range(len(array)):
            state = array[i] if i == 0 else state and array[i]
    elif op == "OR":
        for i in range(len(array)):
            state = array[i] if i == 0 else state or array[i]
    elif op == "XOR":
        for i in range(len(array)):
            state = array[i] if i == 0 else state ^ array[i]
    else:
        return f"input - {op} - not recognized"

    return state


def counting_sheep(a, b):
    t = a, b if len(a) < len(b) else b, a
    pr
    res = lambda x: f"{x[0]}{x[1]}{x[0]}"
    return res(t)


s = "aba"
n = 10


# print(n - n % len(s))


def repeatedString(s, n):
    n1 = n // len(s)
    x = s.count("a")
    x1 = n1 * x
    x2 = s[:n % len(s)].count("a")
    return x1 + x2


print(repeatedString(s, n))
