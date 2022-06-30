from _DoublyLinkedBase import _DoublyLinkedBase
from Empty import Empty

class LinkedDeque(_DoublyLinkedBase):                               # inherited from the base class
    """Double-ended queue implementation based on a doubly linekd list."""
    
    def first(self):
        """Return (but do not remove) the first element of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element                          # real item just after header
    
    def last(self):
        """Return (but do not remove) the last element of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element                         # real item just before trailer
    
    def insert_first(self, e):
        """Add an  element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)   # after header
        
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer
        
    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the end of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)


def main():
    # DLB = _DoublyLinkedBase()
    # DLB._insert_between(1, DLB._header, DLB._trailer)
    # DLB._insert_between(2, DLB._header._next, DLB._trailer)
    # DLB._insert_between(3, DLB._header._next._next, DLB._trailer)
    LDQ = LinkedDeque()
    LDQ.insert_first(2)
    LDQ.insert_last(3)
    LDQ.insert_first(1)
    LDQ.insert_first(0)
    LDQ.insert_last(4)
    print(LDQ.first())
    print(LDQ.last())
    print(LDQ.delete_first())
    print(LDQ.delete_last())

    print(len(LDQ))
if __name__ == '__main__':
    main()