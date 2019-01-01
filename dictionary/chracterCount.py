# character Count

message = 'Respect your elders follow their teachings and it will help you in your tough times'

count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)