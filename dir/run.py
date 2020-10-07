from functools import reduce


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

    def res(x): return f"{x[0]}{x[1]}{x[0]}"

    return res(t)


def repeatedString(s, n):
    n1 = n // len(s)
    x = s.count("a")
    x1 = n1 * x
    x2 = s[:n % len(s)].count("a")
    return x1 + x2


def expanded_form(num):
    num = str(num)
    dec = len(num) - 1
    output = ""
    for i in num:
        if i != "0":
            output += f"{i + ('0' * dec)} + "
        dec -= 1
    return output[:-2].strip()


def to_nato(words):
    nato = {
        "a": "Alpha",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliet",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu"
    }
    words = words.lower().replace(" ", "")

    return
    for w in words:
        if w in nato.keys():
            n_words.append(nato[w])
        else:
            n_words.append(w)

    return ' '.join(n_words).strip()


def highest_rank(arr):
    arr = list(set([(i, arr.count(i)) for i in arr]))
    arr.sort(reverse=True, key=lambda x: x[1])
    rem = lambda x: x[1] == arr[0][1]
    norm_arr = list(filter(rem, arr))
    norm_arr.sort(reverse=True, key=lambda x: x[0])
    return norm_arr[0][0]


# - O(n^2)
def points(dice):
    points = 0
    counter = 0
    counter2 = 0

    straight = [int(i) for i in dice]
    straight.sort()
    for i in range(straight[0], (straight[-1] + 1)):
        counter += i

    is_straight = reduce(lambda x, y: x + y, straight)

    dice2 = list(set([(side, dice.count(side)) for side in dice]))
    dice2.sort(reverse=True, key=lambda k: k[1])

    if len(dice2) == 1:
        points = 50
    elif len(dice2) == 2 and dice2[0][1] == 4:
        points = 40
    elif len(dice2) == 2 and dice2[1][1] == 2:
        points = 30
    elif len(dice2) == 5 and (counter == is_straight):
        points = 20

    return points


print(points("62534"))
