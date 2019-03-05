#Optional Matching with Question Mark

import re

# use question mark for optional pattern in bracket to be searched
optionalRegex = re.compile(r'bat(wo)?man')

book="the adventure of batwoman with batman"

myOption=optionalRegex.search(book)

print (myOption.group())

phoneNumRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

myNum=phoneNumRegex.search('hello vikash is your number 111-1234')
print(myNum.group())