# TO-DO: complete the helper function below to merge 2 sorted arrays
import math


def stitch(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arr_A_index = 0
    arr_B_index = 0

    arr_A_finished = False
    arr_B_finished = False

    for i in range(len(merged_arr)):
        if arr_A_finished or arr_B_finished:
            break
        elif arrA[arr_A_index] < arrB[arr_B_index]:
            merged_arr[i] = arrA[arr_A_index]
            if len(arrA) - 1 == arr_A_index:
                arr_A_finished = True
            else:
                arr_A_index += 1
        else:
            merged_arr[i] = arrB[arr_B_index]
            if len(arrB) - 1 == arr_B_index:
                arr_B_finished = True
            else:
                arr_B_index += 1

    if arr_A_finished:
        for element_index in range(arr_B_index, len(arrB)):
            merged_arr[i] = arrB[element_index]
            i += 1

    elif arr_B_finished:
        for element_index in range(arr_A_index, len(arrA)):
            merged_arr[i] = arrA[element_index]
            i += 1

    return merged_arr


print(stitch([2, 4, 9], [0, 1, 6]), "stitch")
# TO-DO: implement the Merge Sort function below USING RECURSION

[2, 0, 4, 1, 9, 6]


def merge_sort(arr):
    array_of_arrays = []
    for element in arr:
        small_arr = []
        small_arr.append(element)
        array_of_arrays.append(small_arr)

    i = 0

    while i < len(arr) - 2:
        stitch(array_of_arrays[i], array_of_arrays[i + 1])
        i += 2


print(merge_sort([84, 1, 28, 38, 12]), "merge_sort")

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
