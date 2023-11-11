import os

# read data from the filec
filepath = os.path.dirname(__file__)
rfile = filepath+"\\..\\TestData\\txt_file.txt"
wfile = filepath+"\\..\\TestData\\write_file.txt"
try:
    fobj = open(rfile, 'r')
    # read all data from the file
    print("Know current cursor position:", fobj.tell())
    filedata = fobj.read()
    print("Take cursor position to specific char(5th):", fobj.seek(5), fobj.tell())

    # read 1line at a time:
    line_by_line = fobj.readline()

    # read few chars from file
    read_10_chars = fobj.read(10)

    # read all chars from file and display char by char::

    for i in fobj.read():
        print(i)

    # read all data from line by line:
    line_by_line = fobj.readline()
    while (line_by_line):
        print(line_by_line)
        # reading again 2nd line and storing in same variable..
        line_by_line = fobj.readline()

except FileNotFoundError as fn:
    print(f"Check reading file path exists{fobj}:", fn)

# write data into a file
try:
    wobj = open(wfile, 'w')
    wobj.write("hellow user, this is write file handle")
    wobj.close()

    # open existing file and append new data
    aobj = open("E:\writefile.py", 'a')
    aobj.write("this is appending data to the existing data")

except FileNotFoundError as fn:
    print(f"Check reading file path exists{fobj}:", fn)
except Exception as ex:
    print(ex)
