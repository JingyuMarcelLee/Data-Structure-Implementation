import ctypes                                                       # to provide low-level arrays that are not dynamic

class DinamicArray:
    """Implementation of a dinamic array as an ADT in python."""
    
    def __init__(self) -> None:
        """Initialize an empty array."""
        self._n = 0                                                 # count the number of elements stored
        self._capacity = 1                                          # default array max capacity
        self._A = self._make_array(self._capacity)                  # low-level array
    
    def __len__(self) -> int:
        """Return the size of the array."""
        return self._n
    
    def __getitem__(self, k: int) -> object:
        """Return the element at index k. Raise IndexError if invalid index is passed."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj: object) -> None:
        """Add an element to the end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)                        # increase the max capacity of the array by the scale of 2 (dynamic resizing)
        self._A[self._n] = obj
        self._n += 1                                                # increase the number of elements stored
        
    def _resize(self, c: int) -> None:                                           # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)                                     # make a new (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]                                       # shallow copy the referencing to the existing values
        self._A = B                                                 # different reference stored into the original identifier
        self._capacity = c
        
    def _make_array(self, c: int) -> None:
        """Return new low level array with capacity c."""
        return (c * ctypes.py_object)()                             # ctypes.py_object is a type, ctypes.py_object() is an instance
    
    def remove(self, e: object) -> None:
        """Remove element."""
        i = self._index(e)
        B = self._make_array(self._capacity)                        # make new array
        self._n -= 1
        for k in range(0, i):
            B[k] = self._A[k] 
        for k in range(i, self._n):
            B[k] = self._A[k+1]  
        if self._n == self._capacity // 4:
            self._resize(self._capacity // 2)                       # halven the capacity if the num of actual elements are a quarter of the capacity
        self._A = B
        
    def _index(self, e: object) -> int:
        """Find the index of a given element using sequential search."""
        i = 0
        while i < self._n:
            if self._A[i] == e:
                return i
            else:
                i += 1 
        raise ValueError("This element does not exist in this array.")
    
def main():
    print(list(range(1,1)))
    test = DinamicArray()
    test.append(1)
    test.append(3)
    test.append(2)
    print(len(test))
    test.remove(3)
    print(len(test))
    try:
        test.remove(3)
        print("ValueError Uncaught; test fail.")
    except ValueError:
        print("ValueError Caught")
    
if __name__ == "__main__":
    main()