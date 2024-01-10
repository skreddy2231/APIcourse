import pytest
a =3

@pytest.fixture(scope="module")
def fixture_tests():
    print("Start execute Pattern test cases..!!")
    yield
    print("End execute Pattern test cases..!!")


def general_function_args(a,b):
    c = a*b
    print("Given numbers:", c)
    return c

@pytest.mark.Regression
def test_p001_general_function_args(fixture_tests):
    general_function_args(10, 20)  # function input arguments

@pytest.mark.Regression
def functionlist_args(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def test_p002_functionlist_args(fixture_tests):
    functionlist_args(1,3,5)

@pytest.mark.Regression
#keyword agrs , it returns dictionary
def test_p003_function_dict_kwargs(**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs.keys())

@pytest.mark.skipif(a>10, reason="if a is not satisfied, skip this test")
@pytest.mark.Regression
def test_p004_find_total_no_of_fruits(**kargs):
    count =0
    for k,v in kargs.items():
        print(kargs[k])
        count = count + kargs[k]
    print("Total fruits:", count)

@pytest.mark.Regression
def test_p005_cancatinate_values(**kargs):
    str_result = ""
    for k,v in kargs.items():
        print(kargs[k])
        str_result = str_result + kargs[k]
    print("Total fruits:", str_result)

def mixed_outcome(str1, *args, **kargs):
    print(f"I am {str1}")
    for str in args:
        print(f"I am arg: {str}")
    for k in kargs.items():
        print(f"I am kwarg",k)
    return "done"

@pytest.mark.Regression
def test_p006_mixed_outcome():
    mixed_outcome('007', 'agent', firstName='James', lastName='Bond')

@pytest.mark.Sanity
@pytest.mark.Regression
def test_p007_pattren_generator():
    for r in range(0,5):
        for c in range(0, r+1):
            print("*", end=" ")
        print()

    print("====================")
    for r1 in range(6,0,-1):
        for c1 in range(0, r1-1):
            print("*", end=" ")
        print()

    print("=======Triangle 1=============")
    row = 5
    col = row-1
    for r1 in range(0,row):
        for c1 in range(0,col):
            print(end=" ")
        col = col-1
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

# calling function(s)
# result = test_p002_functionlist_args(10, 30, 100, 1)  # args
# print(result)
# test_p003_function_dict_kwargs(apple=5, banana=6)
# test_p004_find_total_no_of_fruits(k=5, k1=2,k3=10)       #17
# test_p005_cancatinate_values(a='Kwargs ',b='are ', c='awesome!')
# test_p006_mixed_outcome('007', 'agent', firstName='James', lastName='Bond')
# test_p007_pattren_generator()

# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# word = "Python"
# x = ""
# for i in word:
#     x += i
#     print(x)

def pytest_pattren():
    str = "triveni"
    str_len = len(str)
    oldchar = ''
    for r in range(0,str_len):
        for c in str:
            oldchar = oldchar + c
            print(oldchar)
        if str == oldchar:
            break


# pytest_pattren()

# equilator triangle
#             *
#            *  *
#           *  *  *
#          *  *  *  *
#         *  *  *  *  *
#        *  *  *  *  *  *
#       *  *  *  *  *  *  *

def equi_Triangle_pyramid_1a():
    rows = 7
    spaceCh = 2*rows
    for r in range(0,rows):
        for c in range(0,spaceCh):
            print(end=" ")
        spaceCh = spaceCh - 1
        for c1 in range(0, r+1):
            print("*", end =" ")
        print()
        #       *
        #      * *
        #     * * *
        #    * * * *
        #   * * * * *
        #  * * * * * *
        # * * * * * * *
#equi_Triangle_pyramid_1a()

# 09/12: riverse equivaluent triangle (homework)
#          * * * * *
#           * * * *
#            * * *
#             * *
#              *
def riverse_equi_Triangle_pyramid_1b():
    rows = 5
    spaceCh = 2*rows
    for r in range(rows, 0, -1):
        for c in range(0, spaceCh):
            print(end=" ")
        spaceCh = spaceCh+1
        for c1 in range(0, r-1):
            print("*", end=" ")
        print()

#riverse_equi_Triangle_pyramid_1b()

# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100

def numbers_pyramid():
    index = 11
    for r in range(1, index):
        for c in range(1, r+1):
            print(r*c, end=" ")
        print()


#numbers_pyramid()


 #   1
 #   2    1
 #   4    2    1
 #   8    4    2    1
 #  16    8    4    2    1
 #  32   16    8    4    2    1
 #  64   32   16    8    4    2    1
 # 128   64   32   16    8    4    2    1

def num2_py():
    #rows = 9
    # for r in range(1, rows):
    #     for c in range(1, r+1):
    #        print(2**c, end=" ")
    #     print("")

    rows = 9
    for i in range(1, rows):
        for j in range(-1 + i, -1, -1):   # j in range(0,-1,-1)
            print(format(2 ** j, "4d"), end=' ')
        print("")
#num2_py()


# def sample():
#     rows = 9
#     for i in range(1, rows):
#         for j in range(-1 + i, -1, -1):
#             print(format(2 ** j, "4d"), end=' ')
#         print("")
#
# sample()

slist = ["books", "fruit", 123, "py", "tests", "students", "c++", 890]
print("length is::", len(slist))



# for ch in range(0,-1,-1):
#     print(ch)

lst = list(range(10))
t1 = [0,1,2,3,4,5,6,7,8,9,54,11]
# print(t1[-2:-9:-2]) # 4,,6,,8,,54
# print(t1[-2:-9:-1])

print(t1[:-9:-1]) # 4,5,6,7,8,9,54,11
print(t1[:-9:-2]) # ,5,,7,,9,,11

print(t1[-1:-1:-1])
print(t1[0:-1:-1])

# print(lst[0:8:3])  #0, 3,6
# print(lst[:-2]) #[0, 1, 2, 3, 4, 5, 6, 7]
# print(lst[:-2:2]) # 0,2,4,6
# print(lst[::4]) # 0,4,8
# print(lst[2:-2]) #[2, 3, 4, 5, 6, 7]
# print(t1[2])

a = 'Stuttgart'
print(a[2:-2]) # uttga
print(a[-2:])  #rt
print(a[5:]) # gart

print(a[::-2]) # t, a,t,u,S
print(a[:-2:-2]) # Stuttga >>> Suta  (# t)


print(a[0:-2]) # Stuttga


slist1 = ["books","c++", 890]
print(slist1[:-2:-2])

# String slicing
String = 'ASTRING'

# Using slice constructor
s1 = slice(3)  # print(String[0:3])
s2 = slice(1, 5, 2) # print(String[1:5:2])
s3 = slice(-1, -12, -2)  # print(String[1:5:2])

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])