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