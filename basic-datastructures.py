
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