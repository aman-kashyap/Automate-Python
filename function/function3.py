#Multiple arguments in function
'''
def add_numbers(*args):
    total=0
    for a in args:
        total += a
    print(total)


add_numbers(2,3,3)
'''

def pyramid(*args):
    for a in args:
        total +=a
    print(pyramid)

pyramid("*")
pyramid("*,*")