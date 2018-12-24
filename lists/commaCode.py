#comma code

def comma(item):
    if len(item) == 1:
        return item[0]
    return '{}, and {}'.format(', '.join(item[:-1]), item[-1])  
        #use .format() and .join() method to concatenate string here 1st {}=" ', '.join(item[:-1])" and 2nd {}=" item[-1] "
        #.join() joins each string with " ', ' "(comma space)

fruits=[]

print("enter some fruits name")

while True:
    name= input()
    if name=="":
        break
    fruits = fruits+[name]

print(comma(fruits))    #use print to display function return value


######### CODE RESIDUE #######

#fruits = ['apple', 'orange', 'pear', 'banana', 'mango']

#print("all fruits are :"+str(fruits[:5]) + "and "+ str(fruits[5]))

#for name in fruits:
#print("all fruits are :"+str(fruits[2:(len(fruits)-5)]) + " and "+str(fruits[len(fruits)-3]))
#print(len(fruits))