# some dictionary methods


birthday={'abhinav':'25 Dec', 'abhishek':'26 Dec', 'ashish':'27 Dec', 'aman':'1 jan', 'shweta':'9 Nov','avantika':'24 Aug'}

for k in birthday.keys():
    print (k)

for v in birthday.values():
    print(v)

for i in birthday.items():      # it return keys and values in tuple form
    print(i)

print(list(birthday.keys()))    # use list() function to print list-like return
print(list(birthday.items()))

# here get() method is used which takes 2 value, the key of the value to retrieve and a fallback value value to return if keys doesnot exist
print("hey jhummi your birthday is on "+ str(birthday.get('avantika', 'unknown')))

print(len(birthday))