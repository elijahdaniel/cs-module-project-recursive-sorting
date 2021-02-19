# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    j = 0
    k = 0

    # keep looping until end is reached for one of the arrs
    for i in range(len(merged_arr)):
        if k > len(arrB) - 1:
            merged_arr[i] = arrA[j]
            j += 1
        elif j > len(arrA) - 1:
            merged_arr[i] = arrB[k]
            k += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        elif arrB[k] < arrA[j]:
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    arrA = arr[: len(arr) // 2]
    arrB = arr[len(arr) // 2 :]

    return merge(merge_sort(arrA), merge_sort(arrB))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    while start < mid and mid < end + 1:
        if arr[start] < arr[mid]:
            start += 1
        else:
            for i in range(start, mid):
                arr[i], arr[mid] = arr[mid], arr[i]

            start += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if r - l <= 0:
        return arr

    mid = l + ((r - l) // 2)

    merge_sort_in_place(arr, l, mid)  # left
    merge_sort_in_place(arr, mid + 1, r)  # right

    merge_in_place(arr, l, mid + 1, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
