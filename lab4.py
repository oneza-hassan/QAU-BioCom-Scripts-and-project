#loops
'''
i=1
while i<6:
    print(i)
    i+=1

i=1
while i<6:
    print(i)
    if i==3:
        break
    print(i)
    i+=1
'''

#infinite loop since condition isnt fulfilling
'''
i=1
while i<6:
    print(i)
    if i==3:
        continue
    print(i)
    i+=1
'''
'''
i=1
while i<6:
    i+=1
    print(i)
    if i==3:
        continue
    print(i)
'''  

#loop
'''
fruits=["kiwi","banana","apple"]
x=len(fruits)
i=0
while(i<x):
    print(fruits[i])
    i+=1
'''
#list
'''
fruits=["kiwi","banana","apple"]
for x in fruits:
    
    if x=="banana":
        continue
    print(x)
for x in fruits:
    
    if x=="banana":
        break
    print(x)

course=["python"]
for x in course[0]: #since list is "python" here so the x will be characters
    print(x)
'''

#range
'''
for x in range(7):
    print(x)

for x in range(3,7):
    print(x)

for x in range(1, 7, 2):
    print(x)
'''

#program to write table of 3
'''
num = 10
for i in range(1, num+1):
    print(i, "x 3 =", i*3)
'''
#or another way
'''
for x in range(3,31,3):
    print(x)

'''
#nested loop
'''
char=["tasty","Red","yellow"]
fruits=["apple","mango","banana"]
for x in char:
    for y in fruits:
        print(x,y)
'''






