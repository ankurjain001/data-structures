import random
arr = [3,5,12,13,14,54,23,43,356,75,23,44,65,21,46,9]


def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge(L)
        merge(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(L):
            arr[k] = R[j]
            j += 1
            k += 1

merge(arr)
print(arr)



