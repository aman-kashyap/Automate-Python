#matching Zero or more pattern using star


import re 


#here the group before * is matched for zero or more times
starRegex = re.compile(r'bat(wo)*man')



#AttributeError: 'NoneType' object has no attribute 'group'
myStar= starRegex.search('here comes batwowowoman')

print(myStar.group())

#matching one or more pattern using plus

#here the group before + is matched one or more times
plusRegex = re.compile(r'bat(wo)+man')
myPlus = plusRegex.search('she is the batwoman')

print(myPlus.group())

#matching specific repetition in the string with curly brackets

repeatRegex = re.compile(r'(Ha){3,5}')  #this is greedy matching it will output max of {}
myRepeatG= repeatRegex.search('Imran Khan: peace gesture . IAF: HaHaHaHaHa')
print(myRepeatG.group())


repeatRegexNonGreedy = re.compile(r'(Ha){3,4}?') #this is non greedy matching with '?' out put min of {}
myRepeatNG= repeatRegexNonGreedy.search('Imran Khan: peace gesture . IAF: HaHaHaHa ')
print(myRepeatNG.group())