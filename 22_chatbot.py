print("Pyhton Program to impliment the calculator.")

num1 = input("Enetr the number A : ")
num2 = input("Enetr the Number B : ")
os = int(input('Enter the Number :\n1 = +\n2 = - \n3 = *\n4 = /'))
if os==1 :
    print(num1 + num2)

elif os==2 :
    print(num1 - num2)

elif os==3 :
    print(num1 * num2)
elif os==4 :
    print(num1 / num2)
else :
    print('Wrong Input')