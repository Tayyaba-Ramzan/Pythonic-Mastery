# String Format in Python

txt1="Welcom {fname} {lname}".format(fname="Tayyaba",lname="Ramzan")
print(txt1)

txt2="Welcomt to {0} {1}".format("Tayyaba","Ramzan")
print(txt2)

txt3="Welcom to {} {}".format("Tayyaba","Ramzan")
print(txt3)

txt4="My value is {a:^10} {b}".format(a=10,b=30)
print(txt4)

txt5="My value is {a:<10} {b}".format(a=10,b=30)
print(txt5)

txt6="My value is {a:>10} {b}".format(a=10,b=30)
print(txt6)
