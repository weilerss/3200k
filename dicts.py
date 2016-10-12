def hist(s):
    """returns the histogram of the characters in s

    >>> hist("AAGGT")
    {'A': 2, 'T': 1, 'G': 2}

    >>> hist("!!xx")
    {'!': 2, 'x': 2}

    """
    results = {}
    for i in s:
        if i not in results:
            results[i] = 1
        else:
            results[i] += 1
    return results         
            
def str_to_int(s):
    """converts a string to an integer value

    >>> str_to_int('s')
    115

    >>> str_to_int('st!ll')
    11511633108108L

    hint: the built in ord and chr functions

    """
    results = ""
    for i in s:
        results += str(ord(i))
    return int(results)

def null_list(length):
    """return a list of all None values of given length

    >>> null_list(3)
    [None, None, None]

    >>> null_list(1)
    [None]

    """
    results = []
    for i in range(length):
        results.append(None)
    return results
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
