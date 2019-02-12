#project table printer
#using list of lists

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(itemsList):
    colWidths = [0] * len(tableData)       #a list colWidths is initialized 

    for i in range(len(itemsList)):
        for j in range(len(itemsList[i])):
            if len(itemsList[i][j]) > colWidths[i]:     #iterate over the itemsList to find longest word in each inner list
                colWidths[i]=len(itemsList[i][j])
    

    #iterate over itemsList and print x value from each innerlist with right justified value
    for x in range(len(itemsList[0])):
        for y in range(len(itemsList)):
            print(itemsList[y][x].rjust(colWidths[y]), end=' ')
        print(' ')

printTable(tableData)


#print(len(tableData))
#colWidths = [0] * len(tableData)
#print(len(colWidths))
#print (colWidths[tableData[1]])
#print(tableData[1])