# pattern matching capablities 

# Grouping

import re 

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')    #create a regular expression object and compile it as raw string 'r'

#sre_constants.error: unbalanced parenthesis at position 9
# The \(and\) escape character in the raw string passed to re.compile() matches actual parenthesis character 
phoneNumRegex2 = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')    #create anothe regular exp.

message = ' abe call kar 112-234-2345 number pe abhi . whatsapp ka number (990) 221-2311 hai '
mynum = phoneNumRegex.search(message)      #pass the string to be searched using search() method 
mynum2 = phoneNumRegex2.search(message)

print ("Phone number Found : " + mynum.group())     #print the phone number

print(mynum.group(1))   #passing 1 in group() will return 1st set
print(mynum.group(0))   #passing 0 or nothing returns whole pattern
print(mynum.group(2))   #passing 2 in group() will return 2nd set

print (mynum2.groups())  # all set of group can be retrived as TUPLE using groups()

stateCode, mobNum = mynum2.groups()
print(stateCode)
print(mobNum)