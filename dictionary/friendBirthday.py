# friend birthday 

birthday={'abhinav':'25 Dec', 'abhishek':'26 Dec', 'ashish':'27 Dec', 'aman':'1 jan', 'shweta':'9 Nov','avantika':'24 Aug'}

while True:
    print("Enter the name to get Date of birth: (press enter to exit)")
    name=input()
    if name=="":
        break
    if name in birthday:
        print(name+'has birthday on'+birthday[name])