# creat the tuple using () this bracket and  tuple is cannot update the vlaues of a tuple 
t = (1)# this is #wrong way to declare a tuple with single element  
t = (1,2,4,5,1,2,4,1)
print(t[1])
print(t.count(1))  #this is a count the repited number 
print(t.index(2)) #this use the check index number 
m1 = input("Enter marks for student number 1 :")
m2 = input("Enter marks for student number 2 :")
m3 = input("Enter marks for student number 3 :")
m4 = input("Enter marks for student number 4 :")
m5 = input("Enter marks for student number 5 :")
m6 = input("Enter marks for student number 6 :")
marklist = [m1, m2, m3, m4, m5, m6 ]
marklist.sort()
print(marklist)

# a= [2,3,5,3,2]
#  a[0]=45
# print(sum(a))

# a= [0,1,2,0,1,0,1,0]
# a.count(0)
# print(a.count(0))