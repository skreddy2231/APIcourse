import os.path
import sys

from numpy import number

absolute_path = os.path.dirname(__file__)
inputfile = 4+"\\..\\Topics.txt"

def handle_exceptions(a,b):
    try:
        a = int(a)
        b = int(b)
        result = a/b
        print("division of a/b:", float(result), " \n modulo of a%b:", (int(a)%int(b)))
    except ValueError as ve:
        print("Please enter numeric values only..\n", ve)
    except NameError as ne:
        print("Name_error occured:\n", ne)
    except Exception as ex:
        print("Oops! runtime error caught!!\n", ex)
    finally:
        print(" <--- I am finally block and executes always! --->")
    print(" *** Execution Done *** \n")
    if a > b:
        try:
            print("b is big", a/b)
        except:
            print("--------------I am 2nd level except block")
            pass
        else:
            print("this stmt executed bez there is no exception in try..")
        finally:
            print("finally data:", a/b)
    try:
        with open(inputfile, 'r') as file1:
            read_txt = file1.read()
            print("file reading part done..")
    except FileNotFoundError as fnf_err:
        print("file not exists:", fnf_err)
    except AssertionError as ae:
        print(ae)
    except Exception as ex:
        sys.exception('sys import lib has an error')
    except ZeroDivisionError as zde:
        print("ZeroDivisionError: integer division or modulo by zero execption..")
    except:
        print("Oops! some exception occured!")


def string_exceptions():
    a = 10
    str = "geeks of geeks tests!!"
    char = 's'
    try:
        print(str)
        print(f"count of {char} occurance in string: {str}", str.count(char))
        print("Remove prefix:", str.removeprefix('gee'), "Given remians string:", str)
        print("Remove suffix:", str.removesuffix('sts'), "Given remians string:", str)
        print("Find str in given string and check returns:", str.find('triveni'))
        print("Find string index and check returns:", str.index('triveni'))
        print("Remove endswith returns bool:", str.endswith('sts'))
    except ValueError as ve:
        print("oops!, ValueError", ve)
    except Exception as ex:
        print("error block")
        sys.exception('sys import lib has an error')
    else:
        print("No error..")
    finally:
        print("finally execute always")


def handle_list_exceptions():
    list1 = [0, 1, 4, 3, 7, 8, 9, 10, 8, 3, 1, 2, 0, 4]
    list1.append("python")
    list1.extend(['py', 'perl', 'c++'])
    list1.remove(1)
    list1.pop(4)
    list1.insert(-1, 'tri')
    print("list1")
    print("Print only duplicate values in list:", list1)


def handle_tuple_exceptions():
    # tuples are immutable, means can not change crud operations
    c1 = ()
    c2 = (1,34,54,78,33,14,56,14)   # 8
    print("min of c2:", min(c2))
    print("max of c2:",max(c2))
    print("length of c2:",len(c2))
    c1 = c1+c2
    print("Get concatenate tuples and get c1:", c1)
    print("reputation:", c1*2)
    print("Indexing access:", c1[-1])
    print("slicing:>>", c1[0:6:2])
    for i in c1:
        print("tuple iteration::", i)
    print("check membership-- 100 in c1:", 100 in c1)
    print("14 in C1>>", 14 not in c1)
    print("both tuples are same(test comparisons):", c1 is c2)

def arthamatic_calculator(choice):
    try:
        param1 = int(input("Enter input number1:"))
        param2 = int(input("Enter input number2:"))
    except RuntimeError as er:    # runtime error means, user send input numbers from cmd..so any expetion caught...goes to runtime error
        print("Please enter integer as number", er)
    match choice:
        case "addition":
            print("Sum of two numbers:", param1 + param2)
        case "subtraction":
            print("Sum of two numbers:", param1 - param2)
        case default:
            print("this is incorrect option")

    print("multiply of two numbers:", param1 * param2)
    return "Given Numbers:",param1 ,param2

def maths_test():
    try:
        arthamatic_calculator("addition")
        with open("sample.txt" 'r') as testfile:
            file1 = testfile
            print("file reading done!")

    except FileNotFoundError:
        print("File error occurred.")
    except NameError as nn:
        print('Only positive integers are allowed', nn)
    except Exception as e:
        print("this is runtime exception", e)
