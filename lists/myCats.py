# using list to get names of cats

catNames =[] #single variable that contain list

while True:
    print ("Enter the cat name"+ str(len(catNames)+1)+ " or enter nothing and press enter to stop :") 
    #here len() gets number of values in list
    name = input()
    if name =="":
        break
    catNames=catNames+[name]    #list concatenation
print ("cat names are:")
for name in catNames:
    print(' '+name)
