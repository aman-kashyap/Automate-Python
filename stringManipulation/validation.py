# string validation

while True:
    print ("Enter your age: ")
    age=input()
    if age.isdecimal():
        print("your age is "+age)
        break
    print ("Enter your age in decimal form")


while True:
    print("Please enter your password")
    password=input()
    if password.isalnum():
        break
    print("your password should consists of only letters and numbers")