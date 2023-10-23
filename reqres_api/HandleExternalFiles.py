handle_flatfile = open('sample.txt', 'r')

second_file = "../FakeRESTApi_swagger/"

for each in handle_flatfile:
    print(each)


# for each in second_file:
#     print(each)
def read_file():
    with open(second_file + "file2.txt") as file2:
        data = file2.read()
        #print(data)
        file2.close()

read_file()

# way2
with open("sample.txt") as file:
    data = file.read()
print(data)