cities=['pune', 'patna', 'gaya', 'benaras', 'prayagraj'] #a list 

print (len(cities)) #prints number of values in the list

for i in range(len(cities)):
    print("index " +str(i)+ " in the cities list is " + cities[i])

print(cities)

print ("Enter the name of your city :")
name = input()
if name not in cities:
    print(name +" is not in the list of cities")
else:
    print("your city is : "+ name)