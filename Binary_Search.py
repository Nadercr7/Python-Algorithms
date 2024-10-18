def binary_search(array, ans):
    left = 0 
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == ans:
            return mid
        elif array[mid] < ans:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
