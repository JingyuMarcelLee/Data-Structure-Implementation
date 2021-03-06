from Empty import Empty

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                              # moderate capacity for all new queues
    
    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return true if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the elment at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        """Remove the element at the front of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None                  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:       # resizing the queue if number of elements is less than 1/4 of the size of the queue
            self._resize(len(self._data) // 2)
        return answer 
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))           # double the array size if the queue is full
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self, cap):                             # assuming cap >= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data                                # saving existing list
        self._data = [None] * cap                       # allocate new list with new capacity
        walk = self._front
        for k in range(self._size):                     # only considering the existing element
            self._data[k] = old[walk]                   # shifting indicies
            walk = (1 + walk) % len(old)                # use old size as %
        self._front = 0                                 # front realigned
                
def main():
    q = ArrayQueue()
    for i in range(1, 11):
        q.enqueue(i)
    print(len(q))
    print(q.first())
    q.enqueue(11)
    print(len(q))
    print(q.first())
    
    q2 = ArrayQueue()
    q2.enqueue(3)
    print(q2.first())
    
if __name__ == "__main__":
    main()

     