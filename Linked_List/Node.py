class _Node:
    """Nonpublic class for respresenting a singly linked node."""
    __slots__ = 'element' ,'_next'      # streamline memory usage (saving these as a tuple instead of a dict to save memory)
    
    def __init__(self, element, next) -> None:
        self._element = element         # user's element
        self._next = next               # next node
        
        
    