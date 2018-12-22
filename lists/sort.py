#some list sorting examples

cities=['pune', 'patna', 'gaya', 'benaras', 'prayagraj']    #a list 

print(cities.index('patna'))   #finding value in list with index() method

cities.append('mumbai') #append() adds a value at the end of list
print (cities)

cities.insert(3,'ayodhya')  #insert() can add a value in list at any position using index 
print(cities)

cities.remove('gaya')   #remove() can delete any value from list
print (cities)

cities.sort()   #sort() arranges list values in ASCIIbetical order
print(cities)

cities.sort(reverse=True)   #sorting in reverse order we can also use different key to sort (key=str.lower)
print (cities)