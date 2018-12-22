#tuples and strings are immutable (its value can't be changed )
#lists are mutable(it can have its value added, removed or changed )

room = ('table', 'chair', 'bed', 'fan', 'light', 'mirror')
print(type(room))
print(len(room))
print(room[0])
#room[1]= 'book'     #TypeError: 'tuple' object does not support item assignment

print(list('hello'))
print(tuple('hello'))
print(str('hello'))