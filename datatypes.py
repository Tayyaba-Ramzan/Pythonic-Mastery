# Data Types in Python

# Mutable DataTypes
# List
# Dictionary

# Immutable DataTypes
# Int
# Float
# Complex
# String
# Tuple
# Set

# Numberic
# Int
a=5
print(type(a))

# Float
a=0.3
print(type(a))

# Complex
a=2+5j
print(type(a))

# string
firstLetter="hello@133"
print(firstLetter, type(firstLetter))

secondLetter="""
                    Python Program
"""
print(secondLetter, type(secondLetter))

# List
list=[10,"tayyaba",2.4]
list[2]=15
print(list,type(list))

# Tuple
tuple=(10,20,"ramzan",2j)
print(tuple,type(tuple))

# Dictionary
dict={
    "courseName":"Python",
    "courseDuration":"3 Month"
}
print(dict,type(dict))
print(dict["courseDuration"])

# Set
s={1,2,3}
print(set,type(set))