# friend birthday 

birthday={'abhinav':'25 Dec', 'abhishek':'26 Dec', 'ashish':'27 Dec', 'aman':'1 jan', 'shweta':'9 Nov','avantika':'24 Aug'}

while True:
    print("Enter the name to get Date of birth: (press enter to exit)")
    name=input()
    if name=="":
        break
    if name in birthday:
        print(name+' has birthday on '+birthday[name])

    else:
        print(name +" is not in birthday dictionary")
        print("what is the birthday of the name given by you")
        bday=input()
        birthday[name]=bday     #here name is key and bday is its value in the birthday dictionary and it saves the information until the program exits
        print("have updated birthday database temporarily")

    