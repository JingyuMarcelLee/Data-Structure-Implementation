from abc import ABCMeta, abstractmethod
class Sequence(metaclass = ABCMeta):
    """Version of collections.Sequence abstract base case (Template method pattern)"""
    
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
        
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j."""
        
    def __contains__(self, val):
        """Return True if val foundi n the sequence, False otherwise."""
        for j in range(len(self)):                  # assuming __len__ exist in a concrete subclass
            if self[j] == val:
                return True
        return False
    
    def index(self, val):
        """Return leftmost index where val is found, raise ValueError otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('the value is not in the Sequence.')
    
    def count(self, val):
        """Return the number of elements equal to its given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k