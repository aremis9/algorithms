
# running time: n*log2(n)
def MergeSort(array):
    n = len(array)
    if n == 1:
        return [array[0]]
    else:
        C = MergeSort(array[:n//2])
        D = MergeSort(array[n//2:])

        return Merge(C,D)

def Merge(C, D):
    i, j, k = 0, 0, 0
    n = len(C) + len(D)
    B = [None] * n

    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else:
            B[k] = D[j]
            j += 1
        k += 1

    while i < len(C):
        B[k] = C[i]
        i += 1
        k += 1

    while j < len(D):
        B[k] = D[j]
        j += 1
        k += 1

    return B


if __name__ == '__main__':

    a = [5, 4, 6, 3, 3, 5, 9, 8, 1, 0, 23, 12, 4, 2, 12]
    b = MergeSort(a)
    print(b)

    a.sort()
    print(a)
    print(a == b)