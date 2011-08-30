#!/usr/bin/env python
def data_diff(first, second, silent=False):
    """
    Compares two python data structures... the kind you might get from json.loads().
    
    Examples:
    
    >>> data_diff('these strings are the same', 'these strings are the same')
    False
    
    >>> data_diff(['these', 'lists', 'are', 'the', 'same'], ['these', 'lists', 'are', 'the', 'same'])
    False
    
    >>> data_diff({'these': 'dicts', 'are': 'the same'}, {'are': 'the same', 'these': 'dicts'})
    False
    
    >>> data_diff({'data_diff': ['can handle', {'nesting of': 'these types'}]}, {'data_diff': ['can handle', {'nesting of': 'these types'}]})
    False
    
    >>> data_diff(['this is', 'a list'], {'this is': 'a dict'})
    types don't match:
    ['this is', 'a list']
    {'this is': 'a dict'}
    True
    
    >>> data_diff(['this list'], ['is shorter than', 'this other list'])
    list lengths don't match:
    ['this list']
    ['is shorter than', 'this other list']
    True
    
    >>> data_diff({'this string:': 'is different than'}, {'this string:': 'over here'})
    values don't match:
    is different than
    over here
    True
    
    >>> data_diff(['this is', 'a list'], {'this is': 'a dict'}, True)
    True
    
    >>> data_diff(['this list'], ['is shorter than', 'this other list'], True)
    True
    
    >>> data_diff({'this string:': 'is different than'}, {'this string:': 'over here'}, True)
    True
    """
    if first == '...' or second == '...':
        return False
    
    if not type(first) == type(second):
        if not silent:
            print "types don't match:"
            print first
            print second
        return True
                
    elif isinstance(first, dict):
        for k in first:
            if k not in second:
                if not silent:
                    print k + " not in second"
                    print first
                    print second
                return True
            if data_diff(first[k], second[k], silent):
                return True
        for k in second:
            if k not in first:
                if not silent:
                    print k + " not in first"
                    print first
                    print second
                return True
            if data_diff(first[k], second[k], silent):
                return True
                
    elif isinstance(first, list):
        if len(first) != len(second):
            if not silent:
                print "list lengths don't match:"
                print first
                print second
            return True
        for i, v in enumerate(first):
            if data_diff(v, second[i], silent):
                return True
    else:
#        if (isinstance(first, unicode) and first[0] == '$') or (isinstance(first, unicode) and second[0] == '$'):
#            return False
#        else:
        if first != second:
            if not silent:
                print "values don't match:"
                print first
                print second
        return first != second
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()