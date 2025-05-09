# May 2025


# python iterators works similarly to cpp and other languages
# key differences are the special python-builtin methods
# which are invoked by default

# java does something similar with the toString() method
# python has the __str__() method aswell as
# the __iter__() method which returns an Iterator Object.
# From this, we can generate an iterator which we can "generate"
# to use in a for-each loop


a = set([2,4,3,2,3,43,4,23,42,3,42,423])
print(a.__str__())

# generate iterator implicitly

for element in a:
    print(element, end="")
print()

# generate iterator explicitley
for element in a.__iter__():
    print(element, end="")
print()
    
# same thing as before, using built-in method
for element in iter(a):
    print(element, end="")
print()
    
# some more expirimenting
it = a.__iter__()
print(it.__str__())
print(max(a))
print(max(it))
print(min(iter(a)))
print(sum(it))
print(min(iter(a)))


# common datastructures have support for iterators!


# lists
a = [1,2,3,2,3,2,3,23] 
print(iter(a))
for i in a:
    print(i)

# tuples
a = (1,2,3,2,3,2,3,23)
print(iter(a))
for i in a:
    print(i)

# sets
a = set([1,2,3,2,3,2,3,23])
print(iter(a))
for i in a:
    print(i)

# dictionary
a = {1:2, 2:4, 5:7}
print(iter(a))
for i in a:
    print(i)

# Impliment a fibonachi number iterator

class FibIterator():
    def __init__(self):

        # initial values, using implicit python tuples
        self.n1, self.n2 = 0, 1

    def __next__(self):
        num = self.n1
        # update the variables
        self.n1, self.n2 = self.n2, (self.n1 + self.n2)
        return num
    
    def __iter__(self):
        # this object itself is an iterator
        # as it impliments the __next__ and __iter__ methods
        return self
    

# print the first 100 fib sequence of numbers
it = FibIterator()
for i in range(100):
    print(i, end=" ")


## Generators
##
## Python includes the "Yield" keyword
## which allows you to create special "Generator Methods"

def fibGenerator():
    # initial values, using implicit python tuples
    n1, n2 = 0, 1

    # indefinite loop? Lol
    while True:
        num = n1
        n1, n2 = n2, (n1 + n2)
        yield num   # new keyword!

# print the first 100 fib sequence of numbers
it2 = FibIterator()
for i in range(100):
    print(i, end=" ")

# wow , both examples work, and do the same thing! 
# the reason for this is -
#
# Python "generators" generate implicit __iter__() and __new__() methods
# which are hinted and constructed using the context that the "yield" keyword provides

print()
print(type(FibIterator())) #Class
print(type(fibGenerator())) #Method/Function

# both will return an "Iterator" type, with different implementation
print(type(it))
print(type(it2))


# Practice Problem

class TriangularNumIterator():
    def __init__(self):
        self.n1, self.n2 = 1, 3

    # had a bug where i accedently typed __new__() lol, spent 10 min fixing this mess
    def __next__(self):
        n = self.n1 # number to be returned
        # update variables
        self.n1, self.n2 = self.n2, self.n2*(self.n2 + 1) // 2 
        return n

    def __iter__(self):
        return self
 
print()
triIt = TriangularNumIterator()
for i in range(7):
    print(str(triIt.__next__()), end=" ")

# implimenting the same algorithm, but with a generator method

def TriangularNumGenerator():
    n1, n2 = 1, 3
    while True:
        n = n1
        n1, n2 = n2, n2*(n2 + 1) // 2
        yield n # this is soo muhc simpler!!!

print()
triIt = TriangularNumGenerator()
for i in range(7):
    print(str(triIt.__next__()), end=" ")


### impliment increasing sum Iterator

class increasingSumIterator():
    def __init__(self):
        self.n = 0
    
    def __next__(self):
        temp = self.n
        self.n += (temp + 1)
        return temp

    def __iter__(self):
        return self #nice lol

print()
sumIT = increasingSumIterator()
for i in range(23):
    print(next(sumIT), end=" ")

# implimentation for Generator

def increasingSumGenerator():
    n = 0

    while True:
        temp = n
        n += temp + 1
        yield temp
    # in the case that function ends, StopIteration exeption is raised

print()
sumIT = increasingSumGenerator()
for i in range(23):
    print(next(sumIT), end=" ")



# Overall, Iterators and Generators both prove usefull for
# iterating over containers, just note that

# __new__()
# __iter__()

# are generated implicitley in - Generators
# are generated explicitley in - Iterators
# this is super cool stuff :)
