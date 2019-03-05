# matching pattern using group and pipe


import re

#using pipe to separate pattern
heroRegex = re.compile(r'Capt. Vikram Batra | Virat Kohli')

hero='Capt. Vikram Batra is real Hero not Virat Kohli'
myhero = heroRegex.search(hero)

print (myhero.group()+" is my HERO ")

# match pattern beginning with same letter in a word.
batRegex = re.compile(r'Bat(man|copter|mobile)')

joker='ha ha ha your Batcopter is toy to me Batman'

myBat= batRegex.search(joker)

print(myBat.group())    #returns first matched character along with prefix
print(myBat.group(1))   #return only matched character
