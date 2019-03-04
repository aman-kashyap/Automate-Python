# matching pattern using group and pipe


import re


heroRegex = re.compile(r'Capt. Vikram Batra | Virat Kohli')

hero='Capt. Vikram Batra and Virat Kohli'
myhero = heroRegex.search(hero)

print (myhero.group())