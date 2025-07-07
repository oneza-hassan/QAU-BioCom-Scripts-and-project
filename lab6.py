#class
'''
class myclass:
    x=5
p1=myclass()
print(p1.x)
'''

#main class / parent class : that have the common attribute of all the others
'''
class person:
    def __init__(self, name, age): #this (constructor func) init func calls automatically when the obj of class is created
        self.names=name            #self refers to the instance of the class. referenced to current obj being operated on
        self.ages=age 
p1=person("oneza", 21)             #p1 and p2 are instances/ distinct objects with unique attributes and identities
print(p1.names, p1.ages)
p2=person("waffle", 22)
print(p2.names, p2.ages) 
'''

#when you want to print arguments together
#parent class

'''
class Person:
    def __init__(self, firstname, lastname, age):
        self.fname_ = firstname
        self.lname_ = lastname
        self.age_ = age

    def __str__(self):
        return f"{self.fname_} {self.lname_} {self.age_}"

    def printname(self):
        print(self.fname_, self.lname_)

    def person(self, gender, height):
        self.gender_=gender
        self.height_=height
        return f"{self.gender_} {self.height_}"

    def welcome(self):
        print("name: ", self.fname_)


p1 = Person("oneza", "alvi", 21)
print(p1)
p1.printname()
print(p1.person("female", "163 cm"))
p1.welcome()
p1.age=22
print(p1.age)
del p1.age #now there is no age so if u print print(p1) it will give error
p1.age=21
print(p1.age) #now no error
'''

#inheritance .... child class

'''
class student(Person):
    pass
x= student("oneza hassan", "alvi", 21)
print (x)
print(x.welcome()) # if we write print with it it will also give none in the output along with the print statement in funct
                   #as welcome func doesnot return any value
x.welcome()        #since we have print in welcome func we dont need to write print again since print only shows the returned value
                   #and in the welcome() no value is returned
print(x.fname_)
print(x.person("female", "165 cm"))
'''
#child class that overrides the __init__() method of parent class

'''
class Student(Person):
    def __init__(self, firstname, lastname, age):   
        self.fname_ = lastname              
        self.lname_ = firstname
        self.age_ = age
y = Student("ONEZA", "ALVI", 21)
y.printname()
'''

# super(): better practice in child class so we dont override the method of parent class

'''
class student_a(Person):
    def __init__(self, firstname, lastname, age):   
        #person.__init__(self, firstname, lastname, age)
        super().__init__(firstname, lastname, age)

z= student_a("hanna", "hassan", 21)
z.printname()
'''

#giving other features to subclass (child class)  that are not in superclass (parent class)

'''
class student_b(Person):
    def __init__(self, firstname, lastname, age, graduationyear):
        super().__init__(firstname, lastname, age)
        self.gradyear=graduationyear

    def combine_info(self):
        print(self.fname_,self.lname_, "graduates in:", self.gradyear, "at the age of:", self.age_)

k= student_b("Oneza", "Hassan", 21, 2024)
print(k)
k.printname()
k.combine_info()
'''
