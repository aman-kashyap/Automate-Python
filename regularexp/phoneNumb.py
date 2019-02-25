#using regular expression to match pattern for phone number

# re module contain all the regularexpression in python
import re 

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')    #create a regular expression object and compile it as raw string 'r'


message = ' abe call kar 112-234-2345 number pe abhi . whatsapp ka number 990-221-2311 hai '
mynum = phoneNumRegex.search(message)      #pass the string to be searched using search() method 
#for mo in range(len(message)):

print ("Phone number Found : " + mynum.group())     #print the phone number