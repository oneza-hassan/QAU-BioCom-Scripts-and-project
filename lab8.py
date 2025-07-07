#modules 
'''
import lab8_module

lab8_module.greeting("oneza")

print(lab8_module.person1["age"])
print(lab8_module.person1.values())
print(lab8_module.person1.keys())     #in all these cases we have to write lab8.module again and again.

'''
# lab8_module is aliased with the name m
'''
import lab8_module as m

m.greeting("oneza")
print(m.person1["age"])
'''

#import a specific function instead of importing the whole module
'''
from lab8_module import greeting as g 
g("oneza")
'''

#example: import platform to check the user system and use other methos 
'''
import platform
x=platform.system()
print(x)
y=platform.architecture()
print(y)
z=platform.uname()
print(z)
k=platform.python_version()
print(k)
x=dir(platform)
print(x)
'''
#example: import datetime module
'''
import datetime as dt

x=dt.datetime.now()
print(x)
print(x.year)
print(x.hour)
print(x.strftime("%p")) #shows am or pm 

y=dt.date(2023,4,11)
print(y)
print(y.strftime("%A")) #shows day

z=dir(dt)
print(z)

'''

#maths basic functions that are built in python
'''
list=[1,2,4,3]
x=min(list)
print(x)
y=max(list)
print(y)

z=abs(-20) #absolute function that makes neg to positive
print(z)

x=pow(4,3) #power func: 4^3=64
print(x)
'''

#to use maths functions that are nt built in to python we have to import maths library
'''
import math as m
a=m.sqrt(81)
print(a)

b=m.pi
print(b)
print(b/2)

print(dir(m))
'''

#regex library: most used library in bioinformatics
'''
import re

str= "regex: widely used library in bioinfo"
y=re.search("lib", str)
print(y)
x=re.search("used", str)
print(x)

y=re.split("\s", str, 2)  #\s is used to denote the spaces 
print(y)

z=dir(re)
print(z)
'''


