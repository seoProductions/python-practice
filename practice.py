# reviewing python after 4 long years 

#input() #returns string by default
# cast input() using float() or int() constructor

l = k = j = 1
# is equivilent to
j = 1
k = j
l = k

#swaping values can be done like this
#this helps avoid creating a temporary value, which comes much in handy
j, k = k, j


## python operands

a = 3 + 7
a //= 2
print( a / 2 )  # float division. aka TRUE (realistic) division
print( a // 2)  # int division.   aka FLOOT (truncated) division

# tip - make numbers more readable using underscores!

a = 234234_234234.2122222_33333
print(a)

# exponentiation
a = 5
a ** 3
print(a)



#########
#########
#########
#########
#########
#########

import random

b = random.randint(4, 8) #inclusive
print(b)

b = random.randrange(4,8) #exclusive 8. generates nubmer from 4 to (8-1)
print(b)

#generate random float from 0 to 1, just like in c++
b = random.random()
print(b)

#set the random seed using
b = random.seed(2342)

# printing using commas

print(b, a, j, l, k)

if j + k >= 0:
    print("the sum of j and k are greater than 1!!!!, their sum is ", j+k)

import sys
#optional exit with exit code!!! wow
#sys.exit(1)

#conditional expressions
# turn this

if (l == 1):
    j = 23
else:
    j = 0

#into this
#THIS IS PYTHONS VERSION OF A TERNARY OPERATOR ?: !!!!!!!!!!!!!! very much english like!

#j = 2  if l == 1 else j = 0

#def max(n1, n2):
#    return n1 if n1 > n2 else n2

#print("The max value from l, k, j, a, and b is: ", max(l, max(k, max(j, max(a, b)))))

# return -1 or 1 only
import time

random.seed(time.time())
print("random int is now ", -1 if random.randint(0,1) == 0 else 1)

#switch statement equivilent for python
month = 2

match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")

#math functions
import math
print(math.sqrt(2))
print(math.atan(math.pi))

#strings in python are simple. You can delcare them using either ' ' or " "

str = "hi"
str = "empty string below me"
str = ""
str = 'also delcare with single quotes!'
str = ''

#convention is to use single quotes for char, and double quotes for any other string
convention = "string"
convention = 'a'    #char

# python uses unicode to represent characters

char = "9"
print(ord(char)) # will print out b

char = 88
print(chr(char)) # will print the uni-code value/ ASCII value

#you can also format print statements by overriding the default end variable of 
# end = "\n"

print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("hey", end="\t")
print("just wanted to say hi!")

#python has a way of checking if a certain substring exists within a string
#these operators evaluate into a boolean expression, being True of False

str = "the other ones are in the other"

print("lol" not in str) # >>> True
print("he" in str)      # >>> True
print("the" not in str) # >>> False


# instead of printing you can use f strings!


print(f"f strings are more avaliable")
print(f"and you can include variables like this one : {a} and this one : {j}")

str = "poaijwdfpojaiwdf"
print(f"starting from the third index, the string above is the following: {str[3:]}")

#you can technically use format like this

print(format("lol this is formated", "12"))


# here is an example of nubmers arranged nice and neatly
a = 12111.123427
print(format(a, ">20.5f"))
a = 432666.123234427
print(format(a, ">20.5f"))
a = 122222221121.123234234427
print(format(a, ">20.5f"))
a = 121111.1234234234234234122347
print(format(a, ">20.5f"))
a = 121123421.122343427
print(format(a, ">20.5f"))
