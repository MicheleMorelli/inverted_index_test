def retrieve(d):
    print_d(d)
    print("INVERTED INDEX:")
    b = inv_index(d)
    print_inv_d(b)

def inv_index(d):
    idx = {}
    for k,v in d.items():
        for element in v:
            idx[element] = idx.get(element, []) + [k]
    return idx

def intersect(d):
    pass

def print_d(d):
    for k,v in d.items():
        print("%s contains %s." % (k,v))

def print_inv_d(d):
    for k,v in d.items():
        print("%s is in pages %s." % (k,v))

def main():
    the_internet = {
    'a' : [1,2],
    'b': [1,2,7,9,7,8,7,7,56,567],
    'c' : [1,2,625,8,4,3,27,7,56,567],
    'd' : [1,2,625,8,4,3,567],
    'e' : [25,53,7,9,567],
    'f' : [56],
    'g' : [53,56,567],
    'h' : [6,567],
    }
    retrieve(the_internet)

if (__name__=='__main__'):
    main()
