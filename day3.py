'''
list 
tuple
for if else?

set
dict
'''
list1 = [1,2,3,[True,False,[11,22,33],["python"]],4,5,6]

'''
True
false
22
python
["python"]
'''
# print(list1[3][0],list1[3][1],list1[3][2][1],list1[3][3][0],list1[3][3])

# print(type(list1)) # cls list

# def add():
#     pass
# add()
# print(type(add))
# tuple1 = (True,)
# print(type(tuple1))

# set is mutable bt value inside the set are immutable
my_set = {"apple","mango","banana"}
new = list(my_set)
print(new)
new.append("cherry")
print(new)




# new = {"cherry"}
# my_set.union(new)
# print(my_set)

result = {"apple","mango","banana","cherry"}
# list>tuple>dict>set  BODMAS

dict1 = {
    1:"one",
    2:"two"
}

'''
if(condition = True/False):
    print("if")
elif(condition = True/False):
    print("elif")
elif(condition = True/False):
    print("elif")
elif(condition = True/False):
    print("elif")

else:
    print("else")

and   or truth tables
TT T  T
TF F  T
FT F  T
FF F  F
'''

'''
Write a program to calculate the electricity bill (accept number of unit from user) according to the 
following criteria :
             Unit                                                     Price  
First 100 units   (0-100)                                             no charge
Next 100 units    (101-200)                                           Rs 5 per unit
After 200 units    (unit>200)                                         Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
30-90-99 = 0
190 = 450

210 = 100*0+500+10*10 = 600

'''
# unit = int(input("Enter you billing unit:  "))
# # unit = int(input("Enter unit"))
# ans = 0
# if(unit<100) : 
#     ans = 0
# elif(unit >100 and unit<=200):
#     ans = (unit-100)*5
    
# else : 
#     ans = (unit-200)*10 + 500
    
# print(ans)

'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
yoe, sal
if yoe>5:
    bonus = 0.05*sal

Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1
numb>0:
num
<0: -1*numb
'''
def add(a,b): #parameters
    return a+b

# print(add(10,15)) #arguments

def show(num = 15):
    return num+15

# print(show())


# *args

# def show(num):
#     return num+15

# print(show())

# fun oops dsa
def display(*child):
    for i in child:
        print(i)

display("jack","sam","rock")


'''
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals.
 The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a 
function that returns the total number of legs of all the animals.

Examples
animals(2, 3, 5) ➞ 36.

animals(1, 2, 3) ➞ 22.

animals(5, 2, 8) ➞ 50.
'''
def animal(ch , c, p):
    return (ch*2 + (c+p)*4)
    
print(animal(2,3,5))

'''
Create a function that takes a list of numbers lst and returns an inverted list.

Examples
invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]

invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]

invert_list([]) ➞ []

def invert_list(lst):
    for i in lst:
        i*-1 
'''

