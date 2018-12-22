#!/bin/bash/python3

print("My Name is ")

for i in range(5):         #for loop uses a variable name (i); a keyword (in); and calls a method --range()
    
    print("jimmy ("+ str(i) +")")

#an equivalent while loop for above program

print("My Name is ")
i=0
while i<5:
    print("jimmy ("+ str(i) +")")
    i=i+1

# for sum of number from 0 to 100
total = 0

for num in range(101):
    total=num+total
    print(total)
print(total)