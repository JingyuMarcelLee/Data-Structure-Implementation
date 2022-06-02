class Range:
    """A class the replicates the behavior of the built-in range() class."""
    
    def __init__(self, start, stop=None, step=1) -> None:
        """Initializing a Range instance."""
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:                        # covering special case of range(n)
            start, stop = 0, start              # this is same as if range(0,n)
        
        
        # calculate the length
        self._length = max(0, (stop - start + step - 1) // step)
        
        # passing the init values
        self._start = start
        self._step = step
        
        
    def __len__(self) -> int:
        """Return the length of the range."""
        return self._length
    
    def __getitem__(self, k: int):
        """Return entry at index k (uses standard interpretation if it is neg)."""
        if k < 0:
            k += len(self)                      # converts negative index
            
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step