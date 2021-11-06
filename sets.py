# sets
# a set is a unordered collection of unique elements
#   a set removes duplicate values

def intersection():
    set1 = {2,3,4}
    set2 = {4,5,6}
    set3 = {3,4,7}

    set4 = set1.intersection(set2, set3) # returns value of set1, which is also included in set2 and set3
    return set4                            

print(intersection())


def add_and_remove():
    myset = {1,2,3,4}
    myset.add(5)     # keep in mind, the add method can only add 1 value to the set
    print(myset)

    myset.update([6,7,8]) # this method adds a a list to a set
    print(myset)

    myset.remove(7) # removes a value of the set // you can also try .discard() 
    print(myset)

add_and_remove()




    