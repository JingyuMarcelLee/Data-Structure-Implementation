class SequenceIterator:
    """An iterator for any sequence types"""
    
    def __init__(self, sequence):
        """Initialize an iterator"""
        self._seq = sequence                # keep a reference to the data
        self._k = -1                        # will increment to 0 when first call of __next__()
        
    def __next__(self):
        """Return the next element of the sequence; if reaches end, raises error"""
        self._k += 1                        # advancing to the next index
        if self._k < len(self._seq):
            return(self._seq[self._k])      # return the data element
        else:
            raise StopIteration()
        
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
def main():
    k = [1,2,3,4]
    seq = SequenceIterator(k)
    for i in range(len(k)):
        print(seq.__next__())
    print(seq)

if __name__ == "__main__":
    main()