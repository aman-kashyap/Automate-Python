#!/bin/bash/python3

# break is used to exit the loop if you donot remove break condition it will keep on executing while statement 
while True:
    print("what is your name?")
    name = input()
    if name == 'your name':
        break
print ("welcome back " + name)


#infinite loop
while True:
    print("you are in infinite loop press ctrl+c to exit loop")