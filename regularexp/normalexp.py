# finding a pattern without using regular expression

#Pattern is 111-111-1111


def isPhoneNumber(numb): #define a function with argument 
    if len(numb) != 12:     #test 1 to check length of argument
        return False
    
    for i in range(0,3):  # take a range
        if not numb[i].isdecimal():     #check if its in decimal form
            return False
    
    if numb[3] != '-':
        return False

    for i in range(4,7):
        if not numb[i].isdecimal():
            return False

    if numb[7] != '-':
        return False

    for i in range(8,12):
        if not numb[i].isdecimal():
            return False

    return True

message = ' abe call kar 112-234-2345 number pe abhi . whatsapp ka number 990-221-2311 hai '

for i in range(len(message)):   #take range as length of message 
    chunk=message[i:i+12]       #pick a set of length from message 
    if isPhoneNumber(chunk):        #put the chunk to check for above def 
        print("phone number found is : "+ chunk)

print("DON")

