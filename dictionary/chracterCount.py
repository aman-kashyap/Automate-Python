# character Count

message = 'Respect your elders follow their teachings and it will help you in your tough times'

count={}    #count dictionary

for character in message:
    count.setdefault(character,0) #the setdefault() method ensures that the key is in count dictionary with a default value 0 
    count[character]=count[character]+1


print(count)