from Empty import Empty

class CircularQueue:
    """FIFO queue implementation using a circularly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing linked node."""
        __slots__ = '_element' ,'_next'        # streamline memory usage (saving these as a tuple instead of a dict to save memory)
        
        def __init__(self, element, next) -> None:
            self._element = element            # user's element
            self._next = next                  # next node
            
    def __init__(self):
        """Create an empty linked queue."""
        self._tail = None                      # representing the tail of the queuee
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
        head = self._tail._next
        return head._element
        
    def dequeue(self):
        """Remove and return the element at the front of the queue (i.e. FIFO)
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:                     # removing the only element
            self._tail = None                   # queue is empty
        else:
            self._tail._next = oldhead._next    # bypass the oldhead
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)            # node will be the new tail 
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tail points to new node
        self._tail = newest                     # update reference
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next       # old head becomes new tail
    
    
def main():
    CQ = CircularQueue()
    CQ.enqueue(1)
    CQ.enqueue(2)
    CQ.enqueue(3)
    print(CQ.first())
    CQ.rotate()
    print("after rotating the queue, the first element becomes: " + str(CQ.first()))
    print(len(CQ))
    
if __name__ == '__main__':
    main()