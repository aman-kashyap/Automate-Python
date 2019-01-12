#some more string methods

spam= "hello world! here i am"
print(spam.startswith('hello')) #checks the string from beginning

print(spam.endswith('ld!'))     ##checks the string from end

cities=['pune', 'patna', 'gaya', 'benaras', 'prayagraj'] #a list 

print(cities)

print(', '.join(cities))    #join() method joins list of string together in a single string value 
print('yo '.join(cities))
#print(type(a))

print(spam.split())         #split() method splits a string into a list

print(spam.split('e'))


print ('hello'.rjust(10,'*'))   #right padding
print('hello'.ljust(10,'*'))    #left  padding
print('hello'.center(20,'='))   #center padding