
#create and empty list in python
firstList = []

firstList = [23,23,23,23,23,42,342,342,34,23,42, 2334]

#lists in python can have all data types, interesting?? I wonder how this works behind the scenes
secondlist = ["abba", 4, 0.3]

#append second list contents to the first list!
range
for i in range(len(firstList)):
    secondlist.append(firstList[i])

print(f"the contents of the second list are the following:\n { secondlist }")


#               Programming Problem 1:
#
#Given list1 as a list and list2 as another list created by replicating list1 a 
#number of times, write a statement to compute and assign it to the variable n.

list1 = [1, 2, 3]
list2 = []

REPLICATION = 23
for i in range(REPLICATION):
    
    list2.extend(list1)


# Solution:

length = len(list1)
n = 0
for i in range(len(list2)):
    #filter out non-matches
    if list1[i % length] != list2[i]:
        break

    if list1[-1] == list2[i]:   # if match last element
        n += 1                  # incriment


print(n)

# OR YOU CAN DO THIS LOl
n = len(list2) // len(list1)

print(min(list2))


## retrieve minimum of first 4 values in list


minimum = list2[0]

for i in range(1, 4):
    minimum = min(minimum, list2[i])

print(f" minimum value of first 4 elements in list2 is: {minimum}! ")


# Swap first and last element

last = list1.pop()
first = list1[0]

list1.append(first)
list1.remove(first)

list1.insert(0, last)

print(list1[:])


#assign true if list has less than 10 elements

value = True if len(list1) < 10 else False
#python looks very similar to english, cpp would write it as

#value = (list1.length() < 10) ? True : False


#lists only support two operators, concatenation + and relication *

print(f"concatonating lists are easy { list1 + list2}")
print(f"replacating lists via multiplication operator { list1 * 4 }\n")

print(list1.__contains__(3))

for i in list1:
    print(i)

# just like java, lists are compared lexiographically

print (list1 >= list2)


###### Python Only!!!!!!!!!!!!!!! ######

print(x for x in range(19) if x < 10) ## will print 0 thru 9
#assign it too!

newlist = [x * 3 for x in range(19) if x < 10]
##  The way this works is 
#
#   python returns a sequence of x's based off of
#   the conditions and iterations specified!
#


#               Programming Problem 2:
#
#Given list1 as a list and list2 as another list created by replicating list1 a 
#number of times, write a statement to compute and assign it to the variable n.
interleaved = []
index1 = 0
index2 = 0
for i in range(max(len(list1), len(list2))): # total elements

    if index1 < len(list1):
        interleaved.append(list1[index1])

    if index2 < len(list2):
        interleaved.append(list2[index2])
# will compare lexiographically
#print(max(list1, list2))

"sdflkj".split



#array shifting trick, shifting left
print( list1[1:] + list1[:1])
#array shifting trick, shifting right
print( [list1[-1]] + list1[:len(list1) - 1])


import statistics

print(f"average of list 1 is { statistics.mean(list1) }")
print(f"average of list 2 is { statistics.mean(list2) }")


def function(ls):
    print("id INSIDE",id(ls))
    return ls

ls = [234,23,2]
print("id ORIGINAL:", id(ls))

ls23 = function(ls)
print("id :", id(ls23))



scores = list(input())