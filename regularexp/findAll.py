#find all matching pattern using findall()

import re

findAllRegex= re.compile(r'\d{3}-\d{3}-\d{4}')

message = ' abe call kar 112-234-2345 number pe abhi . whatsapp ka number 990-221-2311 hai '

mynum=findAllRegex.findall(message)


#AttributeError: 'list' object has no attribute 'group'
#finall() returns a list of string matches
print(mynum)