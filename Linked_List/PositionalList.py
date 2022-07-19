from _DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    
    #------------------------ nested Position class ----------------
    class Position:
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Contructor should not be invoked by the user."""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True iof other does not represent the same location."""
            return not (self == other)             # this would be the opposite of __eq__
        
    #------------------------ utility methods ----------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must e proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node(or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                         # boundery violation
        else:
            return self.Position(self, node)
        
    #------------------------ accessors --------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Returen the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the element of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    #------------------------ mutators --------------------------------
    # override inherited version to return Position instead of None
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes adn return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header(), self._header()._next())
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer().prev, self._trailer())
    
    def add_before(self, p, e):
        """Insert element p into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)      # the inherited element returns element
    
    def replace(self, p, e):
        """Replace the elemnt at Position p with e.
        
        Return the elment formerly at Position p.
        """
        
        original = self._validate(p)
        old_value = original._element            # temporarily store old element
        original._element = e                    # replace with new element
        return old_value                         # return the old element value
    
    
        