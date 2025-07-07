#logical operators
'''
    comparison operator
    greater >
    less <
    equal ==
    not equal !=
    greater, equal >=
    less, equal <=  
'''
'''
x=4
y=5
print(x==y)
print(x<=y)
'''
#take input from user
'''
a=str(input("enter the dna sequence: "))
print(2*a)

z=int(input("enter the age "))
print(z)
agelimit=15
age=int(input("enter age: "))
print("you are overage ", age>=agelimit)
'''
#if else and while
'''
agelimit=15
age=int(input("enter age: "))
i=0
if (age<=agelimit):
    print ("you can take admission")
else:
    while(i<100):
        print("you cant take admission ")
        i=i+1
        if(i==50):
            print("reached fifty")
            break
'''

#loops on list
'''
dna=input("enter the dna seq using A T C and G only: ")
DNA=list(dna)
print(dna)
print(DNA)
updateddna=[]
for k in DNA:
    if(k=="T"):
        print("the base at ", k, " is Thymine")
        updateddna.append(k)
    elif(k=="A"):
        print("the base at ", k, " is adenine")
        updateddna.append(k)
    elif(k=="C"):
        print("the base at ", k, " is cytosine")
        updateddna.append(k)
    elif(k=="G"):
        print("the base at ", k, " is guanine")
        updateddna.append(k)
        break
    else:
        print("the base at ", k, " is not valid dna sequence")
print("final sequence: ", updateddna)
'''

#continue and break
'''
fruits=["orange", "mango", "apple"]
print(fruits)
for x in fruits:
    if x=="mango":
        continue
    print(x)
'''  
   
    

#tuples
''' 
1. ordered collection of elements
2. round brackets ()
3. can store diff datatypes
4. immutable
'''

'''
tup1= (1, "abc", 0.03, True )
print(tup1)
print(tup1[2])
print(type(tup1))
print(type(tup1[2]))
print(len(tup1))
print(type(tup1[0:3]))

tup2= ("world", 12, 7.7, False)

print(tup1+tup2)
print (tup1*2)
tup3= (23,56,222,99)
print (min(tup3))
print (max(tup3))
print ((tup3)*2)
print ((tup1[2])*2) #it does not change the tuple only prints the out put
'''

#list
''' 
1. ordered collection of elements
2. square brackets[]
3. can store diff datatypes
4. mutable
'''
'''
list1= [1, "abc", 0.03, True ]
print(list1)
print(list1[2])
print(len(list1))
print(type(list1[2]))

list2= ["world", 12, 7.7, False]

print(list1+list2)
list1.reverse()
print(list1)

list3= [23,222,56,222,99,222]
print(list3.count(222))
list3.sort()
print (list3)
print(list2+list3)
list1.extend(list3)
print(list1)

list1.append(1)
print(list1)
list1.remove(True)
print(list1)
list3.pop()
print(list3)

dict1={"a":1, "b":2, "c":3}
print(type(dict1))
print(len(dict1))
print(dict1)
print(dict1["a"])
print(dict1.values())
print(dict1.keys())
print(max(dict1.values()))
'''
#dictionary
'''
dict1={"mob":25, "laptop":24, "tab":44}
print(dict1)
dict2={}
dict2["d"]=4
print(dict2)
dict2.update(dict1)
print(dict2)
dict1.update(dict2)
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.pop("tab"))
print(dict1.popitem())
print(dict1)
'''
#sets

'''
1. an unordered and unindexed collection of items
2. declare curly brackets{}
3. one value cant be repeated / no duplicates
'''
'''
set1={12, "samosa", "salad", 44.5, True}
print(type(set1))

set1.add(13)
print(set1)

set2={10, "QAU", "NCB", 2002, False}
print(set1.intersection(set2))
print(set1.union(set2))
'''














    











