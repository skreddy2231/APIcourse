import json

str1 = "GeeksforGeeks"
# o/p:return key which has mini occ char in string  [ K, o, f - s]
dict1 = {}
index = 1


def read_minimum_occuranceChar():
    for i in str1:
        if i in dict1.keys():
            dict1[i] = index + 1
        else:
            dict1[i] = index
    # print(dict1)


read_minimum_occuranceChar()
x = min(dict1, key=dict1.get)
print("Char which has minimum no.of times occured in given string:", x, "\n")

dict2 = {'G': 2, 'e': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}
# given dict, get keys which has odd numbered value?
reslist = []


def fetch_key_has_oddvalue():
    for k, v in dict2.items():
        if (v % 2) != 0:
            reslist.append(k)


fetch_key_has_oddvalue()
print("Key which has odd numbered value:", reslist, "\n")

str2 = "geeks4feeks is No. 1 4 geeks"
general_numset = "0123456789"


def get_wordcount_numbermatch_word_from_str():
    res = 0
    for str in str2.split(" "):
        print("each word:", type(str), " ,and ", str)
        if str in general_numset:
            res = res + 1
    return res


result = get_wordcount_numbermatch_word_from_str()
print("Fetch how many no.of words present with numbers from given string:", result, "\n")

specialchar = "20&%hello_User#123$_*@"
slice_specialchar = list(specialchar)
general_specialchars = "!@#$%^&*()_+?<>:{}~"


def get_wordcount_numbermatch_word_from_str():
    scount = 0
    for str in slice_specialchar:
        if str in general_specialchars:
            scount = scount + 1
    return scount


special_res = get_wordcount_numbermatch_word_from_str()
print("Fetch how many `no.of special chars present from given string:", special_res, "\n")

str33 = "Peter"  # Petr
slicestr = list(str33)


# o/p: length of [n]th char remove..

# print("result remove str:", str33.replace(str33[3],"",1))
def strRead(str, index):
    a = str[: index]
    b = str[index + 1:]
    print(a, " and ", b)
    print(a + b)
    return a + b


a = strRead(str33, 1)
print(a)


def swap_chars():
    swapstr = "14, 625, 498.002"
    # o/p, replace . with command and viceversa
    print("Before swap of string:", swapstr)
    swapstr = swapstr.replace(".,", ",.")
    print("After swap of string:", swapstr)


swap_chars()

loc_str = "geeksforgeeks is best for geeks"
# location of "best"
mainstr = loc_str.split(" ")
for index in range(len(mainstr)):
    # print(mainstr[index])
    if mainstr[index] == "best":
        print("Match word index:", index + 1)

word_str = "geeksforgeeks is best"
# fes
slice_wordstr = list(word_str)
resStr = ""
for ch in slice_wordstr:
    if ch not in "fes":
        resStr = resStr + ch
print(resStr)

mainstr = "xbzefdgstb"
substr = "stb"
print(mainstr.replace(substr, ""))

mainstr = "geeks for geeks"
substr = "for"


def check_substring_Present(mainstr, substr):
    if substr in mainstr:
        print(f'{substr} is exists\n')
    else:
        print(f'{substr} is NOT exists\n')


check_substring_Present(mainstr, substr)

strtest = "abccaaaacbbaa"
slice_strtest = list(strtest)
input_occur_char = "a"


def findlongest_chars_followedby(str, ch):
    temp = 0;
    res = 0
    char_count = 0
    for index in range(len(str)):
        if str[index] == ch:
            temp = temp + 1
            if char_count < temp:
                char_count = temp
            print("char_count", char_count, "and temp", temp)
        else:
            temp = 0
        res = max(res, char_count)
    return res


r = findlongest_chars_followedby(strtest, input_occur_char)
print(f'find inputting char:{input_occur_char} and No.of times, longest char occured:{r}')
