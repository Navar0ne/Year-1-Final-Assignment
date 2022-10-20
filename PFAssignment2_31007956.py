import random                                               
import string                                        ## INCLUDED USER INFORMATION FILE CALLED "data"
import pandas as pd
import os

def mainMenu():                                     # Function to call a menu
    print("\n1) Encrypt text")
    print("2) Extract information from files")
    print("3) Chat with a friend")
    print("4) Exit program\n")

def encryptMenu():
    print("\n1) Encrypt a message and save into a file")
    print("2) Encrypt a file")
    print("3) Decrypt a file")
    print("4) Return to the main menu\n")

def extractMenu():
    print("\n1) View all records")
    print("2) View records by date")
    print("3) View records by user")
    print("4) Count user logs")
    print("5) Back to main menu\n")

def chatMenu():
    print("\n1) Initiate server")
    print("2) Initiate host")
    print("3) Return to main menu\n")

def encryption():                           # Function to run the encryption algorithm

    global table
    encLoop = True

    while encLoop:

        encryptKey = input("Input a number for the key. (Should be between 1 and 53) : ")

        if encryptKey.isdigit():
            encryptKey = int(encryptKey)            # Checks if user input is a digit, if so, converts string to int
            if encryptKey >= 54:            # Prompts user to reselect an encryption key if the input is outside the range
                print("This key is outside of encryption range. Select again.")
                continue
            elif encryptKey <= 0:
                print("This key is outside of encryption range. Select again.")
                continue
            else:
                break
        else:
            print("\nYou have input a non digit key. Select again.")
            continue

    print("Your key is:", encryptKey)

    alphabet = string.ascii_letters + " "            # Creates variable called alphabet containing all upper and lowercase ASCII characters
    shifted = alphabet[encryptKey:] + alphabet[:encryptKey]     # Slices alphabet before and after position of encryption key, shifting the character
    table = str.maketrans(alphabet, shifted)            # creates a mapping table to be translated from later

def decryption():

    global table
    decLoop = True

    while decLoop:

        decryptKey = input("Input a number for the key. (Should be between 1 and 52) : ")

        if decryptKey.isdigit():
            decryptKey = int(decryptKey)
            decryptKey = 53 - decryptKey
            if decryptKey >= 54:
                print("This key is outside of decryption range. Select again.")
                continue
            elif decryptKey <= 0:
                print("This key is outside of decryption range. Select again.")
                continue
            else:
                break
        else:
            print("\nYou have input a non digit key. Select again.")


    print("Your key is:", decryptKey)

    alphabet = string.ascii_letters + " "
    shifted = alphabet[decryptKey:] + alphabet[:decryptKey]
    table = str.maketrans(alphabet, shifted)


print("==  Welcome to Assessment 2 ==")         # START

mainMenu()          # Calls the main menu function

option1 = input("Enter your option: ")

while option1 != 4:                 # Allows me to open a while loop and close it later.

    if option1.isdigit():
        option1 = int(option1)
    else:
        print("\nYou have input a non digit value. Select again.")

    if option1 == 1:            #ENCRYPTION MENU

        keepGoing = True
        while(keepGoing):

            encryptMenu()

            option2 = input("Enter your option: ")
            if option2.isdigit():
                option2 = int(option2)
            else:
                print("\nYou have input a non digit value. Select again.")      # Checks if input is number. If not, restarts the while loop

            if option2 == 1:            #ENCRYPT MESSAGE

                msgToEncrypt = input("\nInput a message to encrypt: ")
                print("\nYour message is: ", msgToEncrypt, "\n")

                encryption()

                encryptedMsg = msgToEncrypt.translate(table)        # Translates the inputted message to the table variable from above
                encryptedMsg = encryptedMsg.replace(" ", "@")       # Replaces the blank spaces with a special character


                print("Encrypted message:", encryptedMsg)

                with open("encryptedMsg.txt", "w") as f:           # Creates a file called encryptedMsg in write mode
                    f.write(encryptedMsg)                 # Writes the content of encryptedMsg to the file

                print("\nEncryption complete.\n")

            elif option2 == 2:          #ENCRYPT FILE

                fileLoop1 = True
                while fileLoop1:

                    fileToEncrypt = input("Input the file name to encrypt: ")

                    try:            # Loop that allows for error checking
                        with open(fileToEncrypt) as f:

                            fileStr  = f.read()
                            print(fileStr)
                            encryption()
                            encryptedFile = fileStr.translate(table)
                            encryptedFile = encryptedFile.replace(" ", "@")

                            with open("encryptedFile.txt", "w+") as f:      # Opens file in write+ mode, meaning you can read and write to it
                                f.write(encryptedFile)

                            print("\nYour new file reads:\n\n",encryptedFile)

                            fileLoop1 = False

                    except IOError:         # Produces an error message when a file can not be found
                        choice = input("File not accessible. Press any to retry, or (x) to return to the menu")
                        if choice != "x":
                            continue            # Resets the while loop
                        else:
                            fileLoop1 = False


            elif option2 == 3:          #DECRYPT FILE

                fileLoop2 = True
                while fileLoop2:

                    fileToDecrypt = input("Input the file name to decrypt: ")

                    try:
                        with open(fileToDecrypt) as f:

                            fileStr  = f.read()
                            print(fileStr)
                            decryption()
                            decryptedFile = fileStr.translate(table)
                            decryptedFile = decryptedFile.replace("@", " ")

                            with open("decryptedFile.txt", "w+") as f:      # Opens file in write+ mode, meaning you can read and write to it
                                f.write(decryptedFile)

                            print("\nYour new file reads:\n\n",decryptedFile)

                            fileLoop2 = False

                    except IOError:     # Produces an error message when a file can not be found
                        choice = input("File not accessible. Press any to retry, or (x) to return to the menu")
                        if choice != "x":
                            continue
                        else:
                            fileLoop2 = False

            elif option2 == 4:          # RETURN
                break           # Breaks the while loop, allowing code to continue
            else:
                print("\nInvalid option.\n")

    elif option1 == 2:          #VIEW RECORDS

        keepGoing2 = True
        while(keepGoing2):

            extractMenu()

            option3 = input("Enter your option: ")

            if option3.isdigit():
                option3 = int(option3)
            else:
                print("\nYou have input a non digit value. Select again.")

            if option3 == 1:            #ALL RECORDS

                print("\n== View All Records ==\n")

                with open("data.txt", "r") as f:           # Opens a file as read only
                    data = f.readlines()        # Reads the lines in the document individually
                    cleanedData = pd.DataFrame([item.strip().split(",") for item in data], columns=["Name", "Date"])
                    #^ Creates a PANDAS dataframe out of the raw text file & splits it into names and dates
                    
                    print(cleanedData)

            elif option3 == 2:          #RECORDS BY DATE

                with open("data.txt", "r") as f:
                    data = f.readlines()
                    cleanedData = pd.DataFrame([item.strip().split(",") for item in data], columns=["Name", "Date"])

                    print("\n==View Records By Date==\n")

                    dateSearch = input("Input a date with the format dd/mm/yy: ")
                    specDate = cleanedData.loc[cleanedData["Date"] == dateSearch] # Locates the date column of the dataframe specifically
                    if specDate.empty:      # Checks if the column is empty
                        print("\nNo record(s) found!\n")
                    else:
                        print(specDate)

            elif option3 == 3:          #RECORDS BY USER

                with open("data.txt", "r") as f:

                    data = f.readlines()
                    print("\n== View Records by User ==\n")
                    cleanedData = pd.DataFrame([item.strip().split(",") for item in data], columns=["Name", "Date"])

                    uniqueNames = pd.unique(cleanedData['Name'])        # Finds unique values in the Name column and saves them to a variable
                    print("Names available :\n",uniqueNames)

                    print("\n== Getting List of Dates by Name ==\n")
                    #Store the groups as the key in a dictionary
                    #We prepare a dictionary : Key is the name, Values are lists for students
                    dates_and_names = {key:[] for key in uniqueNames}

                    #Getting all dates for each name
                    for key in dates_and_names:
                        studentsName = cleanedData.loc[cleanedData['Name'] == key] #getting records for a specific name
                        dates_and_names[key] = list(studentsName['Date']) #getting the name col and update the dictionary

                    print(studentsName)

                    print("List of dates by names:\n")
                    for key in dates_and_names:
                        print(key)
                        print("=================")
                        for item in dates_and_names[key]:
                            print(item)
                        print("=================")

            elif option3 == 4:          #COUNT USER LOGS

                with open("data.txt", "r") as f:

                    data = f.readlines()
                    print("\n== Count User Logs ==\n")
                    cleanedData = pd.DataFrame([item.strip().split(",") for item in data], columns=["Name", "Date"])

                    users = cleanedData['Name'].value_counts()      # Counts the amount of entries each name has

                    print("\n== User login counter ==\n",users)

            elif option3 == 5:          #RETURN
                break
            else:
                print("\nInvalid option.\n")


    elif option1 == 3:          #CHAT APPLICATION
        keepGoing3 = True
        while keepGoing3:

            chatMenu()
            option4 = input("Enter your option: ")
            if option4.isdigit():
                option4 = int(option4)
            else:
                print("\nYou have input a non digit value. Select again.")

            if option4 == 1:
                os.system("start cmd /k pythonServer.py") # Opens a cmd window for the server file to be executed
            elif option4 == 2:
                os.system("start cmd /k pythonClient.py") # Opens a cmd window for the client file to be executed
            elif option4 == 3:
                break
            else:
                print("\nInvalid option.\n")


    elif option1 == 4:          #EXIT PROGRAM
        break
    else:
        print("\nInvalid option.\n")

    mainMenu()
    option1 = input("\nEnter your option: ")

print("Thank you for using this program.")      # Thank you message