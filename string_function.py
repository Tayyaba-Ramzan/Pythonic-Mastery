# String Function in Python

# find()
department="Software Engineering"
# print(department.find("w")) 
print(department.find("i",13))
# print(department.find("z")) return -1

# index()
print(department.index("S"))
# print(department.index("x")) error

# isalpha()
alpha=("Hi")
print(alpha.isalpha())

# isdigit()
digit="123"
print(digit.isdigit())

# isalnum()
isNum="hello123"
print(isNum.isalnum())