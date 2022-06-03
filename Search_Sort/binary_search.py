import pprint

from pygments import highlight

def binary_search(data, target, low, high) -> bool:
    """Return True if the target is found in the list"""
    
    if low > high:
        return False
    else:
        mid = low + ((high - low)//2)
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

def binary_search_nonRecursive(data, target) -> bool:
    """Return True if the target is found in the list (non-recursive)"""
    high = len(data) - 1
    low = 0
    while low < high:
        mid = low + ((high-low)//2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

d = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(d, 3, 0, 9))
print(binary_search_nonRecursive(d, 3))
