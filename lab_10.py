#file handling
'''
open(): Opens a file and returns a file object.
read(): Reads the contents of a file.
write(): Writes data to a file.
close(): Closes a file object.
with: A context manager used to automatically close a file after use.
mode: The mode in which a file is opened (e.g., read mode, write mode).
seek(): Changes the current position of the file pointer.
tell(): Returns the current position of the file pointer.
flush(): Flushes the write buffer of a file object.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
os: A module that provides a way to interact with the operating system, including file handling operations.
'''
#r, w, a, x
'''
#f=open("oneza_DEMO.txt","x")
#f.close()
'''

'''
f=open("oneza_DEMO.txt","w")
f.write("ONEZA's first file created\n")
f.write("BIO COMPUTING 2\n")
f.close()
f=open("oneza_DEMO.txt","a")
f.write("lab 10: file handling\n")
f.write("demo file\n")
f.close()
f=open("oneza_DEMO.txt","r")
print(f.read(10))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline(3))
'''
#exception handling use try and except block to handle errors
'''
try:
    f=open("oneza_DEMO.txt","r")
    print(f.read(10))
    print(f.readline())
    print(f.readline())
    print(f.readline(3))
    f.close()
except:
    print("an exception has occured")
finally:
    print("\nExecuted: no errors")
'''
#exception handling: when file already exists but we are opening with x
'''
try:
    f=open("oneza_Demo.txt","x")
    f.close()
except:
    print("File already exists!")
'''
#exception handling: when reading a file that doesnot exit
'''
try:
    f=open("BS_Demo.txt","r")
    print(f.read(10))
    print(f.readline())
    print(f.readline())
    print(f.readline(3))
    f.close()
except:
    print("create the file first")
finally:
    f=open("oneza_DEMO.txt","r")
    print(f.read(10))
    print(f.readline())
    print(f.readline())
    print(f.readline(6))
    print(f.readline())
    print(f.readlines())
    f.close()
'''
#to delete a file from system, import os (operatingsystem) module
#to del a directory use rmdir : os.rmdir("directory name")
'''
#ff=open("filetobedeleated.txt","x")
#ff.close()

import os
os.remove("filetobedeleated.txt")
'''
#use loops to make change to file
'''
f=open("oneza_DEMO.txt","r")

#create another file to save the content of oneza_DEMO.txt that does not have the line "demo file", and include all other lines
#e=open("DEMO2.txt","w")
#e.close()

for x in f:
    #if(x=="demo file"): one way is by using condion
    #other way by using the keyword

    #if x.find("demo file")!= -1: #it will find only the first "demo file"
      # print(x)

    if "demo file" in x:
        continue
    print(x)
        #e.write(x)

f.close()

'''


    






