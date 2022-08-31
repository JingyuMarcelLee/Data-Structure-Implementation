class PriorityQueueBase:
    """Abstract base case for a priority queue."""
    
    class _item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __It__(self, other):
            return self._key < other._key   # compare items based on the key values min Heap in this case
        
    def is_empty(self):   # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0