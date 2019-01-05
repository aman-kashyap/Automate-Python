#string isX() methods

greet="Hello World!"
print(greet.islower())          #turns true if all letter is in lowercase
print(greet.upper().isupper())  #turns true if all letter is in uppercase

print('hello'.isalpha())        #turns true if there is only letter and no blank
print('hello1'.isalpha())

print('hell1234'.isalnum())         #turns true if there is only letter, number and no blank 

print('1234'.isdecimal())           #turns true if there is only numerical characters

print ('     '.isspace())            #turns true if there is only space,tab or newline characters

print('Hello 2S@A 1Am'.istitle()) #turns true if string consists of  words beginning with uppercase and rest with lowercase
        #if uppercase is followed by any character and by lowercae letter it turns false 





