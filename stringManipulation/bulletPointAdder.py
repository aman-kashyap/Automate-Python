#!/bin/bash/python3

#Adding bullet points to the start of lines

#copy some lines of text 

import pyperclip

pyperclip.copy("Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars")
# we can either use above line or comment it and just copy some lines of text 

text = pyperclip.paste()

lines=text.split('\n')  #splits text in clipboard at \n

for i in range(len(lines)):     #it loops through all indexes in the "lines" list.
    lines[i] = '* ' + lines[i]  #it will add star and space to each stinng in "lines" list.


text= '\n'.join(lines)      #it generates list of string value from list of lines / list of lines are passed into join() method
                            #to get a single string joined

pyperclip.copy(text)
#the output is copied in your clipboard . you can paste it in file which you are editing, it will display the output with * and space at the beginning of a line
print(pyperclip.paste()) #prints the output NOT NEEDED

