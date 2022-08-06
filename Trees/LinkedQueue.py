from Empty import Empty

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing linked node."""
        __slots__ = '_element' ,'_next'        # streamline memory usage (saving these as a tuple instead of a dict to save memory)
        
        def __init__(self, element, next) -> None:
            self._element = element            # user's element
            self._next = next                  # next node
            
    def __init__(self):
        """Create an empty linked queue."""
        self._head = None
        self._tail = None
        self._size = 0                         # number of elements in the queue
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Retirm (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element             # front aligned with head of the list
        
    def dequeue(self):
        """Remove and return the element at the front of the queue (i.e. FIFO)
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None
        return ans
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)            # node will be the new tail 
        if self.is_empty():
            self._head = newest                 # special case as previous is empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference
        self._size += 1

def main():
    LQ = LinkedQueue()
    LQ.enqueue(1)
    LQ.enqueue(2)
    LQ.enqueue(3)
    print(LQ.dequeue())
    print(LQ.dequeue())
    print(len(LQ))
    
if __name__ == '__main__':
    main()