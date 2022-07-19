from PositionalList import PositionalList

class FavoritesList:
    """List of elements ordered from the most frequently accessed to least."""
    
    
    #------------------------- nested _Item class ------------------------
    class _Item:
        __slots__ = '_value', '_count'                # stearmline the memory usage
        def __init__(self, e):
            self._value = e                           # the user's element                                           
            self._count = 0                           # access count initially 0 (will use this value to sort the linked list)
            
    #------------------------ nonpublic utilities --------------------------------
    def _find_position(self, e):
        """Search for element e and return its Position (None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.fisrt():
            count = p.element()._count
            walk = self._data.before(p)
            if count > walk.element()._count:          # must shift forward
                while (walk != self._data.first() and
                        count > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) # delete/reinsert
                
    #------------------------- public methods -----------------------------
    def __init__(self) -> None:
        """Create an empty list of favorites."""
        self._Data = PositionalList()                  # will be list of _item instances
        
    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0
    
    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                      # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))      # if new, place at the end
        p.element()._count += 1
        self._move_up(p)                                # consider move forward
        
    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)                      # try to locate exsiting element
        if p is not None:
            self._data.delete(p)                        # if found, delete
            
    def top(self, k):
        """Generate sequence of top k elements in terms of accesss count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                        # element of list is _Item
            yield item._value                            # report user's element
            walk = self._data.after(walk)

def main():
    A = FavoritesList()._Item("A")
    B = FavoritesList()._Item("B")
    C = FavoritesList()._Item("C")
    D = FavoritesList()._Item("D")
    myList = FavoritesList()
    myList._Data.add_first("A")
    myList._Data.add_last("D")
    myList._Data._insert_between("A", "D", "C")
    myList._Data._insert_between("A", "C", "B")
    myList.access("A")
    myList.access("A")
    myList.access("A")
    myList.access("A")
    myList.access("C")
    myList.access("C")
    myList.top(2)
    print(myList._Data.last())

if __name__ == '__main__':
    main()                