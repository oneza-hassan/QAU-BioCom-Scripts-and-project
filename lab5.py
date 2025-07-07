# functions
""" reduce line of code
can use code again and again with calling"""

'''
def myname():
    print ("this is oneza")

myname()
'''
#arguments in function
'''
def weather(today):
    print ("the weather today is: ", today)

a=input("hows the weather today? sunny/ rainy or cold? ")
weather(a)
weather("sunny")
weather("rainy")
weather("cloudy")
'''

#multiple arguments in function
'''
def OOTD(top,bottoms):
    print ("Top: ",top, " and bottoms: ", bottoms)

OOTD("button up", "wide pants")
OOTD("kurta", "trowsers")
'''

#when func dont know how many arguments should be there. use asterisk *
# * is ok with any num of arguments

'''
def my_course(*module):
    print("my major modules are: ", module[5], " , ", module[2], " , ", module[4])
    print("all subjects: ", module)
    print ("this class is : ", module[-1])
    print(module[1:3]) #slice

my_course("proteomics","sys bio","graphics","modeling and simulation","DSA", "biocompII")
'''

#when position of argument doesnt matter
'''
def major_course(module1, module2, module3):
    print("my major module at NCB is : ", module1)  
    print("my major module at CS is : ", module2)

major_course(module2="Graphics and visualization",module3="sys bio",module1="biocompII")

major_course("Graphics and visualization","sys bio","biocompII")
'''

#assignment value to argument in func body
'''
def my_country(country = "Pakistan"):
  print("I am from " + country)
  alphabets=list(country)
  for i in alphabets:
    total_char= len(country)
  print(country, " has ", total_char, " characters")  

my_country()
my_country("Korea")
a=input("enter your country: ")
my_country(a)
'''

#function argument given by user can overwrite the actual values
# side note: if we use print when calling the function too then it will give None since we never used the return function in body
'''
def siblings(sib1= "shaheer", sib2="malahim", sib3="areeb"):
    print("the middle sibling is: ", sib2)

siblings()
siblings("malahim", "areeb", "shaheer")
siblings(sib2= "shaheer", sib1="malahim", sib3="areeb")
print(siblings()) #this will give None as well as an output cz no return func in def
'''

#pass array / list in function argument
'''
def birthdays(BDay):
    for i in BDay:
        print ("BDAYs : ", i)
        
BDays=[25,27,25]
birthdays(BDays)
'''

#if we use return in func body then to print result we have to use print funcion 
#when we call the func since we are returning the value
#by using return we can use the output value in the program and have changes to it
'''
def percentage(marksobt, total):
    return (marksobt/total)*100

print (percentage(400, 650))
x=percentage(400, 650)+20
print(int(x))
'''

#return value
'''
def percentage(marksobt, total):
    result=(marksobt/total)*100
    if result>80:
        return result, "you are accepted to GKS"
    else:
        return result, "better luck next time"
a=int(input("marks obtained: " ))
b=int(input("total marks: "))       
result, message = percentage(a, b)
print(result)
print(message)
x=result+10
print("bonus: ", x)
'''

#for returning multiple values 
'''
def percentage(marksobt, total):
    grade= (marksobt/total)*100
    scholarship= "GKS SCHOLARSHIP"
    return(grade,scholarship)

result= percentage(400, 650)
print(result[0])
print(result[1])
print(result[0]+20)
print(result[0],result[1])
print(result)
'''

#recursive functions
''' 
    . A recursive function is a function that calls itself.
    . solve problems that have a recursive structure, such as computing factorials,
      generating Fibonacci sequences, or traversing a tree or graph data structure.
    . Recursive functions must have a base case that provides a stopping condition for the
      recursion. Without a base case, the function will continue to call itself infinitely, resulting
      in a stack overflow error.
'''
'''
def recursive_func(k):
    if k>0:
        result= k+ recursive_func(k-1)
        print(result)
    else:
        result=0
    return result

recursive_func(4)
'''
#pass to skip the function
'''
def rest(r):
    pass
'''
#recursive function example fibonacci series
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(result)
        return result

result = fibonacci(4)
print("Final result:", result)

for x in range(7):
    print (fibonacci(x))
'''
