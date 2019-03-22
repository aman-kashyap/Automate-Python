#find all matching pattern using findall()

import re

findAllRegex= re.compile(r'\d{3}-\d{3}-\d{4}')  #here findall() will return list of string as no group is here
                                                # it will return list of tuples of string if there is group
                                                # (r'(\d{3})-(\d{3}-\d{4})') 2 groups in here

message = ' abe call kar 112-234-2345 number pe abhi . whatsapp ka number 990-221-2311 hai '

mynum=findAllRegex.findall(message) #using findall() to match all pattern and save its value in mynuum object.


#AttributeError: 'list' object has no attribute 'group'
#finall() returns a list of string matches
print(mynum)