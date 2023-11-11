import os

folderpath = os.path.dirname(__file__)
txt_file = folderpath+"\\..\\Training\\DataFiles\\demo.txt"

readmode = open(txt_file, mode= 'r')
print("1) Get readmode txt file content --- \n", readmode.read())
readmode.close()

writemode = open(txt_file, mode= 'w')
print("\n2) Get writemode txt file content, this write overwrite existing data: --- \n")
writemode.write("I am overwrite existing data....\n welcome to py course..this is writemode")
writemode.close()


appendmode = open(txt_file, mode= 'a')
print("Get appendmode txt file content with append to the existing data: --- \n")
appendmode.write("\n3) I am appending to the existing data ....\n are you progressing py tests?..")
appendmode.close()

read_write_mode = open(txt_file, mode= 'r+')
print("read_write_mode, first read:", read_write_mode.read())
print("\n 4) Get read_write_mode txt file content with append to the existing data: --- \n")
read_write_mode.write("\n 4) this is read and then write content")
read_write_mode.close()

write_read_mode = open(txt_file, mode= 'w+')
print("Get write_read_mode txt file content with append to the existing data: --- \n")
write_read_mode.write("\n 5) here trucating existing data and write newly!!")
write_read_mode.close()


# with open(txt_file, mode='r') as txtfile:
#     my_txt = txt_file.read()
#
# def handle_flatfile(flatfile):
#        print(flatfile)
#
#
# handle_flatfile()
