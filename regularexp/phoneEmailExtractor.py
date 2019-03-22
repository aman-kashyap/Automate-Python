# extract phone number and email 

# copy text in clipboard
# create regular expression for phone number and email address
# find all the phone number and email id 
# 

import re

phoneNumRegex = re.compile(r'\+\d{2}\s+\d{10}')

emailAddRegex = re.compile(r'\w+\.\w*\@\w+\.\w+')


info=" 9-01-21  Email  	  divya.barathi@vvdntech.in  Mobile  	  +91 8883082299  Skype  	  Divya Barathi +91 5667788919 Active Projects 1. VVDN_TRNG    Direct Reports"

phnum = phoneNumRegex.findall(info)
emadd = emailAddRegex.findall(info)

#print(phnum)
#print(emadd)

matches[]

for 

