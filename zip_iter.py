# Zip Function in Python Programming 

first_list=[10,20,30]
second_list=[40,50,60]

for n,m in zip(first_list,second_list):
    print(n,m)

# Ignored:
list_one=[1,2,3,4,5]
list_two=[6,7,8,9,10,11,1,2,13,134,15,16]

for a,b in zip(list_one,list_two):
    print(a,b)    

# for() Loop:
t=len(first_list)
for h in range(t):
    print(first_list[h],second_list[h])