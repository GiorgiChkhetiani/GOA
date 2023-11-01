def find_smallest_int(arr):
    smallest = arr[0]
    for element in arr : 
        if element < smallest:
            smallest = element 
    return smallest