#using rjust() ljust() center() padding methods to print a table


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, '.')+str(v).rjust(rightWidth))

stuff = {'rope':1, 'torch':6,'gold coin':42,'dagger':1,'arrow':12}
printPicnic(stuff, 10,5)
printPicnic(stuff, 20,5)
