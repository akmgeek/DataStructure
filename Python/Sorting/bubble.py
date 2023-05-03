def bubbleSort(arr):
    """
    Sorts a given list using the bubble sort algorithm.

    Parameters:
    arr (list): The unsorted list to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    for i in range(1,len(arr)):
        for j in range(len(arr)- i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr



L1 = [9, 5, 2, 7, 1, 3, 8, 4, 6,12]
L2 = [23, 1, 17, 9, 3, 8, 12, 5, 21, 16]
L3 = [54, 29, 13, 46, 82, 37, 91, 68, 75, 41]
L4 = [33, 19, 55, 42, 87, 26, 14, 66, 70, 91, 10]


print(bubbleSort(L1))   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubbleSort(L2))   # Output: [1, 3, 5, 8, 9, 12, 16, 17, 21, 23]
print(bubbleSort(L3))   # Output: [13, 29, 37, 41, 46, 54, 68, 75, 82, 91]
print(bubbleSort(L4))   # Output: [10, 14, 19, 26, 33, 42, 55, 66, 70, 87, 91]
