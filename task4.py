class userNumber (int):
    def multiplyTable (self):

        #initialize future str to print
        # (start it with a tab so that there's empty space in the high left corner)
        tableToPrint = "\t"

        #initizlize the list where all the rows for the table will be stored
        finalTable = []

        #init first row to go on till user's number
        firstRow = []

        for i in range(1, self +1):
            firstRow.append(i)

        #add first row to final nested list
        finalTable.append(firstRow)

        #multiply all numbers to create further rows for the table
        for i in range(1, self+1):
            rowForTable = []
            rowForTable.append(i)
            for y in firstRow:
                rowForTable.append(i*y)
            finalTable.append(rowForTable)

        #iterate over the recieved nested list to convert it into the string to print in console
        for el in finalTable:
            for number in el:
                tableToPrint += str(number)
                #add tab to prettify the output
                tableToPrint += "\t"
            tableToPrint += "\n"
        return tableToPrint


testNum = userNumber(9)
testTable = testNum.multiplyTable()
print(testTable)
