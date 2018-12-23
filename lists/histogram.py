#histogram

def histogram(number):  #define a function 
    for i in number[:]: #here i picks all values in list.
        print('*'*i)    

p=[]    #initialize a list

print ("enter some integer for making histogram and to stop press 0")

while True:
    
    integer=int(input()) #takes integer input for the list 
    if integer ==0:
        break               #breaks loop to exit condition and completes list p[]
    p=p+[integer]           #list concatenation

print("your list contains : "+str(p))
histogram(p)    #calling function

#print("you have entered following integers")
#for integer in p:
#    print(integer)
#p=[2,3,4,5]
#histogram(p)

#print(p[:])
#print (len(p))
#for i in p[:]:
#    print('*'*i)

#for p[:] in range(len(p)):
#    print ('*'*p[:])
