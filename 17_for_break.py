for i in range(5):
    if i == 3:
        break
    else:
        print(i)

#Write a program to loop into a string "Hello World!" and break the loop when the letter is "o", otherwise keep printing the letters.
for i in 'Hello World!':
    if i == 'o':
        break
    else:
        print(i)