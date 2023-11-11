def set_examples():
    # set is a mutable
    # don't allow duplicates
    # un-indexed
    # un-ordered
    s1 = {1,42,56,46,3,6,1,42}
    print("Original set:", s1)  # it prints in an un-order based.
    print("add elements:", s1.add(76))
    print("update <bulk> elements:", s1.update({47,10,200}))
    print("delete random element:", s1.pop(), "\n after remove s1:", s1)
    print("remove randon element:", s1.remove(46), "\n and then s1:", s1)

    # set operations < union , intersection, difference, issubset, is>
    s2 = {1,3,2,4,5,10}
    s3 = {4,5,6,7,8,9,20}
    print("Union data:", s2.union(s3))
    print("Intersection data:", s2.intersection(s3))
    print("difference data from two sets:", s2.difference(s3))  # it prints only S2 unique data by remove common data
    print("superset data::", s2.issuperset(s3))
    print("subset data::", s2.issubset(s3))






set_examples()