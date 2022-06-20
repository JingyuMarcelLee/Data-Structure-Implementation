def insertion_sort(A):
    """Sort the list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):                      # goes from 1 to n-1
        cur = A[k]                                  # this is the current element that will be inserted
        j = k                                       # find the correct index for the current element
        while j > 0 and A[j-1] > cur:               # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                                  # cur is in the right place now