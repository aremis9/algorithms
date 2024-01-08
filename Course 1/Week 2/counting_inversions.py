
# running time: n*log2(n)
def CountInv(array):
    n = len(array)
    if n == 0 or n == 1:
        return ([array[0]], 0)
    else:
        (C, left) = CountInv(array[:n//2])
        (D, right) = CountInv(array[n//2:])
        (B, split) = CountSplitInv(C, D)

        return (B, left + right + split)

def CountSplitInv(C, D):
    i, j, k = 0, 0, 0
    n = len(C) + len(D)
    B = [None] * n

    # number of inversions
    s = 0

    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else:
            B[k] = D[j]
            j += 1
            s += (len(C) - i)
        k += 1

    while i < len(C):
        B[k] = C[i]
        i += 1
        k += 1

    while j < len(D):
        B[k] = D[j]
        j += 1
        k += 1

    return (B, s)


if __name__ == '__main__':

    nums = []
    with open("IntegerArray.txt", "r") as file:
        for line in file:
            nums.append(int(line.rstrip("\n")))
    
    # print(nums)

    # # a = [1, 3, 5, 2, 4, 6]
    # a = [6, 5, 4, 3, 2, 1]
    # # a = [1, 3, 2]
    b = CountInv(nums)
    print(b[1])

    # a.sort()
    # print(a)
    # # print(a == b)