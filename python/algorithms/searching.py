def binary_search(arr: list, low: int, high: int, elem: int) -> int:
    """Binary search."""
    if high >= low:
        mid = (low + high) // 2
        if elem == arr[mid]:
            return mid
        elif elem < arr[mid]:
            return binary_search(arr, low, mid-1, elem)
        elif elem > arr[mid]:
            return binary_search(arr, mid+1, high, elem)
    else:
        return -1
