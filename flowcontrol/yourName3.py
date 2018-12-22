#!/bin/bash/python3

# using continue and break condition in while loop 

while True:
    print ("what is your name ?")
    name = input()
    if name != 'aman':
        continue
    print ("hi aman! please enter your password:")
    password = input()
    if password == 'qwer':
        break
print ("you are authorised!")