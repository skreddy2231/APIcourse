def test_pattern():
    for r in range(1,6):
        for c in range(6,r,-1):
            print("5", end=" ")
        print()

#test_pattern()

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

def test2_patt():
    col =0
    max =6
    for r in range(max,col,-1):
        for c in range(col,r+1):
            print(c, end="")
        #max = max-1
        print()

# test2_patt()

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9
def odd_pyramid():
    rows = 5
    i = 1
    while i <= rows:
        j = 1
        while j <= i:
            print((i * 2 - 1), end=" ")
            j = j + 1
        i = i + 1
        print('')

# test local
#odd_pyramid()

def test_p007_pattren_generator():
    for r in range(0,5):
        for c in range(0, r+1):
            print("*", end=" ")
        print()

    print("====================\n")
    for r1 in range(6,0,-1):
        for c1 in range(0, r1-1):
            print("*", end=" ")
        print()

    print("=======Triangle 1=============")
    row = 5
    col = row-1
    for r1 in range(0,row):
        # below for loop for space
        for c1 in range(0,col):
            print(end=" ")
        col = col-1
        # below for loop for prog logic
        for c1 in range(0, r1+1):
            print("*", end =" ")
        print()

    print("=======Triangle 2=============")
    row1 = 5
    col1 = row1 -1
    for r1 in range(row1, 0, -1):
        for c1 in range(row1-r1):
            print(' ', end='')
        col1 = col1-1
        for c1 in range(r1-1):
            print("*", end=" ")
        print()


test_p007_pattren_generator()