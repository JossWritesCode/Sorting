# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr)):
        index_of_smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_of_smallest]:
                index_of_smallest = j
        smallest = arr[index_of_smallest]
        arr.pop(index_of_smallest)
        arr.insert(i, smallest)

    return arr


print(selection_sort([10, 2, 4, 7, 23, 1]),
      "selection sort")  # result [1, 2, 4, 7, 10, 23]


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    last_index = len(arr) - 1

    did_sort = True

    while did_sort == True:
        i = 0
        did_sort = False
        while i + 1 <= last_index:
            if arr[i + 1] < arr[i]:
                smaller_element = arr[i + 1]
                arr.pop(i + 1)
                arr.insert(i, smaller_element)
                did_sort = True
            i += 1

    return arr


print(bubble_sort([10, 2, 4, 7, 23, 1]), "bubble_sort")
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
