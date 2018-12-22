#!/bin/bash/python3

# a import module contain an import key word; name of module (here random) more module name can be added by using comma 

import random,math,sys

for i in range(3):
    print(random.randint(1,100)) #using random module 


while True:
    print('Type exit to exit')
    response=input()
    if response=='exit':
        sys.exit()              #using sys module
    print('you typed '+ response)
    break                       #using break to exit fromm loop even if you donot type 'exit'

print (math.sqrt(625))