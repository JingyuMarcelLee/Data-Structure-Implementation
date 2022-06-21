class LinkedStack:
    """LIFO Stack using a singly linked list."""
    
    #-------------------------Nested _Node class ----------------------------------------------------------
    class _Node:
        """Nonpublic class for respresenting a singly linked node."""
        __slots__ = '_element' ,'_next'        # streamline memory usage (saving these as a tuple instead of a dict to save memory)
        
        def __init__(self, element, next) -> None:
            self._element = element           # user's element
            self._next = next                 # next node
        
        
    #-------------------------Stack methods ----------------------------------------------------------------
    def __init__(self) -> None:
        """Create an empty stack."""
        self._head = None                     # head node
        self._size = 0                        # number of elements in the stack
        
    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return Trie if the stack is empty."""
        return self._size == 0
    
    def push(self, e) -> None:
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1
        
    def top(self) -> object:
        """Return the element at the top of the stack.
        
        Raise exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('There are no elements in the stack.')
        return self._head._element              # top of the stack is at head of the list
    
    def pop(self) -> object:
        """Remove and return the element from the top of the stack (LIFO).
        
        Raise exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('There are no elements in the stack.')
        ans = self._head._element
        self._head = self._head._next            # bypass the former top node
        self._size -= 1
        return ans
        
        
def main():
    linkedList = LinkedStack()
    linkedList.push(1)
    linkedList.push(2)
    linkedList.push(3)
    print(linkedList.pop())
    
    
if __name__ == '__main__':
    main()