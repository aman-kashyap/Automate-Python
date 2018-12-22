#refrence, copy, deepcopy

import copy

def room(item):
    item.append('pillow')

home = ['table', 'chair', 'bed', 'fan', 'light', 'mirror']
room(home)
print (home)    #item()and home() have different refrences but they refer same list

theatre=copy.copy(home)     #theatre( and ) home() refer to different list
theatre[2]=55
print (home)
print(theatre)


#farm= copy.deepcopy(theatre)
#farm[3]=88
#print (farm)
#print(theatre)