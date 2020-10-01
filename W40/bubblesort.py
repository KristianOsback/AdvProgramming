from issorted import issorted

def bubblesort(lst):
    """ Computes a bubble-sort

    >>> bubblesort([5, 2, 3])
    [2, 3, 5]
    >>> bubblesort([])
    []
    >>> bubblesort([1])
    [1]
    """
    lst = (list(lst))
    
    changes = True
    while changes:
        changes = False
            for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                actionCount += 1
            
    return lst 

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("yeah")
        
print("noget")