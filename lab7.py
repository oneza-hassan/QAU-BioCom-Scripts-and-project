#iteration
'''
obj1=("apple","mango","banana")
print(type(obj1))
'''
#to show elements one by one by conventional method
'''
for i in obj1:
    print(i)
'''

#show item one by one using iterator function
'''
element=iter(obj1)  
print(next(element))
print(next(element))
print(next(element))
'''

#print the alphaphets of elemnts at 0 index ie apple
'''
myobj=iter(obj1[0])
print(next(myobj))
print(next(myobj))
print(next(myobj))
print(next(myobj))
print(next(myobj))
'''
#print the character of string at 1 index ie mango
'''
myobj1=iter(obj1[1])
next(myobj1)
print(next(myobj1))
print(next(myobj1))
print(next(myobj1))
print(next(myobj1))
'''

#iterator obj in class and functions
'''
class number:
    def __iter__(self):   #the funct starting from double under score is dunder/magic/special functions. they run automatically
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass=number()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
#this will send in to infinite loop since my iter will never stop and no condition is given
'''
for x in myiter:
        print(x)
'''

#how to use for loop and not go in infinite loop
'''
class num:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a += 1
            if self.a>6:
                raise StopIteration()
            else:
                return x
        else:
            raise StopIteration()

myclass=num()
myiter=iter(myclass)
for x in myiter:
        print(x)
    #   if x==6:    # u can either break in the for loop or in the next function 
     #      break   #use break wheneven you have to stop at a particular point

'''

#scope 
'''
global x  #this x is defined in program outside the function so its accessible everywhere
x=1000
print("x=",x)

y=200  
def numinscope():

    z=500
    print("z=", z)   #this x is only defined in this scope
    global x        #we have to use global every time so it change the value everywhere after it
    x=20
    print("x=",x) 
    global y
    y=10
    print("y=", y)
    global k
    k=500
    print("k=", k)

numinscope()
print("y=",y)
print("x=",x)   #notice when we print x in line 96 it prints 1000 but here it will give 20 since in line 102 we globally changed x
print("y=",y)
print("k=",k)   #it will not give error since global k has scope in all program even if it is defined in a func
'''
#scope another example
'''
def myfunc():
    x = 200
    def innerfunct():
        print(x)
    innerfunct()
myfunc()
'''






