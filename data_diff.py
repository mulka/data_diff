def data_diff(first, second):
    if isinstance(first, dict):
        if not isinstance(second, dict):
            print "types don't match"
            print first
            print second
            return True
        else:
            for k in first:
                if data_diff(first[k], second[k]):
                    return True
            for k in second:
                if data_diff(first[k], second[k]):
                    return True
                
    elif isinstance(first, list):
        if not isinstance(second, list):
            print "types don't match"
            print first
            print second
            return True
        else:
            if len(first) != len(second):
                print "list lengths don't match"
                print first
                print second
                return True
            for i, v in enumerate(first):
                if data_diff(v, second[i]):
                    return True
    else:
        if first == '...' or second == '...':
            return False
#        elif (isinstance(first, unicode) and first[0] == '$') or (isinstance(first, unicode) and second[0] == '$'):
#            return False
        else:
            if first != second:
                print "values don't match:"
                print first
                print second
            return first != second
    return False