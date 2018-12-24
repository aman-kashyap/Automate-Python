#comma code

#fruits = ['apple', 'orange', 'pear', 76, 'banana', 'mango']

#print("all fruits are :"+str(fruits[:5]) + "and "+ str(fruits[5]))

fruits=[]

print("enter some fruits name")

while True:
    name= input()
    if name=="":
        break
    fruits=str(str(fruits)+name+", ")

#for name in fruits:
print("all fruits are :"+str(fruits[2:(len(fruits)-5)]) + " and "+str(fruits[len(fruits)-3]))
print(len(fruits))