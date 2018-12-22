#The collatz Sequence

def collatz(number):
    if number % 2 == 0:
        a=number//2
        print(a)
        return a
    elif number % 2 != 0:
        a= (3*number+1)
        print (a)
        return a

print ("Enter a number :")

try:
    n=int(input())
except ValueError:
    print("enter a valid integer")
#n=input()
while n!=1:
    n=collatz(n)