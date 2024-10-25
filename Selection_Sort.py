# Function to find the smallest element in an array and return its index
def findSmallest(arr):
    # Assume the first element is the smallest
    smallest = arr[0]
    smallest_idx = 0
    # Get the length of the array
    length = len(arr)
    # Loop through the array starting from the second element
    for i in range(1, length):
        # If the current element is smaller than the smallest so far
        if arr[i] < smallest:
            smallest = arr[i]         # Update smallest to the current element
            smallest_idx = i          # Update smallest_idx to the current index
    # Return the index of the smallest element
    return smallest_idx

# Function to sort an array using the selection sort algorithm
def Selection_Sort(arr):
    # Get the length of the array
    length = len(arr)
    # Create a new array to store the sorted elements
    newarr = []
    # Loop through the array until it's empty
    for i in range(length):
        # Find the index of the smallest element in the array
        smallest = findSmallest(arr)
        # Remove the smallest element from the original array and add it to the new array
        newarr.append(arr.pop(smallest))
    # Return the sorted array
    return newarr



"""
Explanation:

    -The `findSmallest` function identifies the smallest element in the array and returns its index.
    
    -`Selection_Sort` uses `findSmallest` to iteratively find the smallest element, remove it from `arr`, and add it to `newarr`.
    
    -This process continues until `arr` is empty, resulting in `newarr` being the sorted array.

"""
