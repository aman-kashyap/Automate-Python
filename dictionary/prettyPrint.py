# Pretty Printing

# module pprint gives access to function pprint() and pformat() that ensure a pretty print of dictionary value  
import pprint

message = 'Respect your elders follow their teachings and it will help you in your tough times.'

count={}    #count dictionary

for character in message:
    count.setdefault(character,0) #the setdefault() method ensures that the key is in count dictionary with a default value 0 
    count[character]=count[character]+1


pprint.pprint(count)    #the print output looks cleaner

print(pprint.pformat(count))