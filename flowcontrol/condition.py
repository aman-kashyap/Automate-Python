#!/bin/bash/puthon3
# difference between if and while loop
# 1 assign spam = 0; begin if condition; assign spam again for while condition; check output
spam = 0
if spam < 5 :
    print ('hi !')
    spam = spam + 1


#spam = 0
# while loop is reccursive unless the condition is met but if loop checks condition ones and then exits loop
while spam < 5 :
    print ('hello !')
    spam=spam + 1