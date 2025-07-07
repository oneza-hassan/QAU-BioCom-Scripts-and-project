#regex module

import re

'''
x= "plasmodium is the cause of malaria. "
y= re.findall("l", x)
print(y)

y= re.search("l", x)
print(y)

print(y.endpos)

y=re.split("\s", x)
print(y[5])

y=re.sub("is", "IS", x)
print(y)
'''

#string formatting
'''
x= "{1} is absent today. {0} needs to work hard" 
print(x.format("maham", "rida"))
x= "{a} is absent today. {b} needs to work hard" 
print(x.format(a="maham", b="rida"))
print(x.format(b="aima", a="hareem"))

'''

#exception handling #when there are error in file and we want program to keep executing
#try and except (exception) block dont terminate prog
'''
try:
    print(x)
except NameError:
    print("an name exception has occured")
except:
    print("an exception has occured")

'''

#try except else finally
'''
x=2
try:
    print(x)
except:
    print("an exception has occured")
else:                          #it will run if except is not executed
    print("run file")
finally:                        #it will run even if prog went in all block or in none.
    print("have a nice day")

'''
#customize the exception
'''
try:
    print(x)
except:
    raise NameError("please define X")
'''
#check the type
'''
x="hello"
if not type(x) is int:
    raise TypeError("X should be int")
'''
#in old version input was not used but raw_input is used so 
#if using an old code we have to change certain things else there will be error
'''
x=input("name: ")
print(x+" alvi")
'''



