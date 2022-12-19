os = int(input('Enter the Number :\n1 = +\n2 = - \n3 = *\n4 = /'))
num1 = int(input('enter the number A :'))
num2 = int(input('enter the number B :'))
if os ==1:
    print(num1+num2)
elif os == 2 :
    print(num1-num2)
elif os == 3:
    print(num1*num2)
elif os == 4 :
    print(num1/num2)

else:
    print('wrong input')
dict = {
    'name':'kartik',
    'collage':'parul university',
    'div':'5b1',
    'city':'vadodara'
}
print(len(dict))
print(dict)
print(dict['name'])
dict.update({'name':'kartik patel'})
print(dict['name'])

print(dict)