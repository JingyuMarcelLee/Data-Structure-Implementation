class Vector:
    """Represents a vector in a multidimensional space. Implied method overriden to simulate vector properties."""
    
    def __init__(self, d: int) -> None:
        """Create d-dimensional vectors of zeros. (like zeros() in matlab)"""
        self._coords = [0] * d
        
    def __len__(self) -> int: 
        """Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j: int) -> int:
        """Return the jth coordinate of the vector."""
        return self._coords[j]
    
    def __setitem__(self, j: int, val: float) -> None:
        """Set the jth coordinate of vector to a given value"""
        self._coords[j] = val
        
    def __add__(self, other):
        """Return sum of two Vectors(since this is not radd, onle works when the vector object is on the left side of the + sign)"""
        if len(self) != len(other):                         # relies on __len__()
            raise ValueError('dimensions do not agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other) -> bool:
        """Return True if the vector has same coordinates and dimension as other."""
        return self._coords == other._coords
    
    def __ne__(self, other) -> bool:
        """Return true if the vector differs from other"""
        return not self == other                            # relies on __eq__()
    
    def __str__(self) -> str:
        """Produce string representation of a vector."""
        return '<' + str(self._coords)[1:-1]+'>'            # using list representation
    
if __name__ == '__main__':
    V1 = Vector(5)
    V2 = Vector(5)
    print(V1==V2)
    for i in range(len(V1)):
        V1.__setitem__(i,1)
    
    for i in range(len(V2)):
        V1.__setitem__(i,2)
    
    print(V1+V2)