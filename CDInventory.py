#------------------------------------------#
# Title: CDInventory.py
# Desc: A CD inventory program
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# ALarson, 2021-Nov-13, Converted 2D list to list of dictionaries
# ALarson, 2021-Nov-14, Changed menu code blocks to match dictionary functionality
# ALarson, 2021-Nov-14, Added functionality for deleting and loading data
#------------------------------------------#

# Declare variables
strChoice = '' # User input
dictTbl = []  # list of dictionaries to hold data
dictRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object



#Create file and load existing data (if any)into memory first
print('The Magic CD Inventory\n')
print('Current inventory is:')

#Load in previously saved data to memory, if any, create a file if not
objFile = open(strFileName, 'a')
objFile.close()
print()
objFile = open(strFileName, 'r')
for row in objFile:
    print(row)
    lstRow = row.strip().split(',')
    dictRow= {'ID': int(lstRow[0]), 'Album': lstRow[1], 'Artist': lstRow[2]}
    dictTbl.append(dictRow)
objFile.close() 

# Get user Input and run menu items
while True:
    # 1. Display menu allowing the user to choose:
    print('MENU')
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Load existing data from file (similar to above)
        objFile = open(strFileName, 'r')
        for row in objFile:
            print(row)
        objFile.close()    
        
    elif strChoice == 'a':
        # Add data to the table as a dictionary(2d-list) each time the user wants to add data
        strID = (input('Enter an ID: ')) 
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID) #change the stringID to an integer
        dictRow = {'ID':intID, 'Album':strTitle, 'Artist':strArtist} #pack the dictionary with user input
        dictTbl.append(dictRow)  #append the newly created dictionary to the existing 2d table
        print(dictRow)
        confirm = input('Is this correct? Y/N: ')
        if confirm.lower() == 'y':
            print()
            print('Great - Back to Menu')
            print()
        elif confirm.lower() == 'n':
            print()
            print('If you\'d like to delete a CD from the inventory, press [d].')
            print()
        else:
            confirm = input('Is this correct? Y/N: ')
            print('Great - Back to Menu')
            
            
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in dictTbl:
            print(*row.values(), sep=', ')
        print()   
            
    elif strChoice == 'd':
        # Allow the usser to delete an entry
        selection = int(input('Which ID would you like to delete? '))
        for row in dictTbl:
            if selection == row['ID']:
                dictTbl.remove(row)
                print('You have removed your data...remember to Save.\n')
                                
                     
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in dictTbl: #for each dictionary in the 2d table
            strRow = ''
            for item in row.values(): #for each item in the dictionary that are values
                strRow += str(item) + ', '
            strRow = strRow[:-2] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Your data is saved.')
        print()
    else:
        print('Please choose either l, a, i, d, s or x!')

