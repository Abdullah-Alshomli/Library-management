# extra function
def bookList():                       # this function will make a list thats contain the information of each book in a singl part.
    file = open("booksInfo.txt", "r")
    bookList = []                     # this the list that will contain the information of each book in a singl part.
    for line in file:
        line = line.strip().split(",")
        bookList.append(line)
    file.close()
    return bookList

# menu function
def menu():                            # this function will display the menu to the user.
    print()
    print("Library Management System")
    print("=" * 30)

    print("1. Print books info")
    print("2. Search a book")
    print("3. Add new book")
    print("4. Remove a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

    print("=" * 30)
    option = input("Enter your choice: ")
    return option

# function-1
def PrintBooksInfo():                  # this function will print the info of each book.
    booksNumber = 0
    file = open("booksInfo.txt","r")
    bookInfo = file.read().strip().split("\n")
    books = []
    for book in bookInfo:                   # to make a list that contains the information for each book in a single part.
        books.append(book.split(","))
        booksNumber = booksNumber + 1
    print()
    print()
    print()
    print()
    print("Total",booksNumber,"books:")
    print("-"*46)

    for book in books:                      # printing the information of each book.

        print("serial#:",book[0])
        print("title:",book[1])
        print("number of authors:",len(book[2].split(":")))
        print("Price:",book[3])
        print("total copies:",int(book[4])+int(book[5]))
        print("-"*46)

    file.close()

# function-2
def search():                          # this function will search for a book and display its information.
    booklist = bookList()
    bookfound = False
    records = 0
    titleOrAuthor = input("Enter (t) to search by title or (a) to search by author name: ") #  giving the user the choice to input
    if titleOrAuthor == "t":                                                                ## name of a book or an author.
        title = input("Enter the title: ")
        for book in range(0,len(booklist)):        # to test each book individually.
            info = booklist[book]
            realTitle = info[1]
            if title.lower() in realTitle.lower(): # allowing the user to input capital or small characters.

                bookfound = True                   #  assigning book found to true To stop the program
                             ## from printing "No matched record found" in the main function.

                if records == 0:                   # to make sure "Matched records: " only print once
                    print()
                    print("Matched records: ")
                    records = 1
                print("serial#: ", info[0])
                print("title: ",info[1])
                print("authors:")
                authors = info[2]
                authors = authors.split(":")        # to get each author individually.
                for author in range(len(authors)):
                    print(" - " + authors[author])
                print("price: ",info[3])
                print("copies in library: ", info[4] )
                print("borrowed copies: ", info[5])
                print("-" * 47)

            elif bookfound != True:                 # to test if a book was found or not.
                bookfound = False




    elif titleOrAuthor == "a":                       #  this part is similar to the first part we just changed the index
        author = input("Enter author name: ")        ## to search for the author name instead of the title.
        for book in range(0,len(booklist)):
            info = booklist[book]
            name = info[2]
            if author.lower() in name.lower():
                bookfound = True

                if records == 0:
                    print()
                    print("Matched records: ")
                    records = 1
                print("serial#: ", info[0])
                print("title: ",info[1])
                print("authors:")
                authors = info[2]
                authors = authors.split(":")
                for each in range(len(authors)):
                    print(" - " + authors[each])
                print("price: ",info[3])
                print("copies in library: ", info[4] )
                print("borrowed copies: ", info[5])
                print("-" * 47)

            elif bookfound != True:
                bookfound = False

    return bookfound

# function-3
def addBook():                         # this function will add a new book to “booksInfo.txt”.
    validInfo = True
    serial = input("Enter serial number: ")
    bookTitle = input("Enter book title: ")
    authors = []
    author1 = input("Enter name of author 1: ")
    authors.append(author1)
    stop = False
    autherCounter = 2
    while stop == False:
        author = input("Enter name of author " + str(autherCounter) + " (Enter q to finish): ") #  to ask the user to input multiple
        autherCounter = autherCounter + 1                                                       ## authors.
        if author != "q":
            authors.append(author)
        else:
            stop = True

    if len(authors) > 1:                                # to make a string that contains the names of authors separated by ":".
        nameCounter = 0
        while nameCounter == 0:
            authorsSTR = authors[0]
            nameCounter = 1

        if nameCounter == 1:
            for name in authors[1:len(authors)]:
                authorsSTR = authorsSTR + ":" + name

    else:
        authorsSTR = authors[0]                         # if only one author was inputted.


    try:
        price = float(input("Enter book price: "))
        priceSTR = str(price)
    except ValueError:
        price = False                                   # if the price is not a float or empty.

    try:
        numBooks = int(input("Enter number of book copies: "))
        numBooksSTR = str(numBooks)
    except ValueError:
        numBooks = False                                  # if the numBooks is not an integer or empty

    list = bookList()




    print()
    # serial number error
    for line in range(0,len(list)):
        if serial in list[line]:                           # to check if the serial number already exists before.
            print("Error: serial number is already used")
            validInfo = False

    if len(serial) != 5:                                   # to check if the serial number has 5 digits.
        print("Error: serial number should be 5 digits")
        validInfo = False

    # Title error 2
    if bookTitle == "":
        print("Error: Title should not be empty")
        validInfo = False

    # authors names error 3
    if "" in authors:                                      # to check if author name is not empty.
        print("Error: names of all authors should not be empty")
        validInfo = False

    # price error 4
    if price == False:
        print("Error: price should be a valid float number")
        validInfo = False

    # number of copies error 5
    if numBooks == False:
        print("Error: number of copies should be a valid int number")
        validInfo = False


    if validInfo == True:                 # to check if every enterd information was valid.
        file = open("booksInfo.txt","w")                                                # write the information of each book.
        list.append([str(serial), bookTitle, authorsSTR, priceSTR, numBooksSTR, "0"] )
        for bookinfo in list:
            file.write( bookinfo[0]+","+ bookinfo[1]+","+ bookinfo[2]+","+ bookinfo[3]+","+ bookinfo[4]+","+ bookinfo[5]+"\n")
        file.close()


        print("New book was added successfully")

# function-4
def RemoveBook():                      #  this function will remove a book from the file” booksInfo.txt”.
    serialNumber = input("Enter book serial number to remove: ")
    file = open("booksInfo.txt","r")
    records = 0
    listBooks = bookList()
    for book in range(0,len(listBooks)):           # to check if the book is in the file.
        info = listBooks[book]
        realSerial = info[0]
        if serialNumber in realSerial :

                if records == 0:                   # to make sure "Matched records: " only print once.
                    print()
                    print("Matched records: ")
                    records = 1
                print("serial#:", info[0])
                print("title:",info[1])
                print("authors:")
                authors = info[2]
                authors = authors.split(":")        # to get each author individually.
                for author in range(len(authors)):
                    print(" - " + authors[author])
                print("price:y",info[3])
                print("copies in library:", info[4] )
                print("borrowed copies:", info[5])
                print("-" * 47)
                borrowedCopies = int(info[5])

                yesOrNo = input("Deleting the book .. Are you sure (y/n): ") # giving the user the choice to cancel the operation.
                if yesOrNo == "y":
                    file = open("booksInfo.txt","w")
                    for bookinfo in listBooks:                               # to remove the information of the book from the file.

                        if bookinfo[0]==serialNumber and bookinfo[-1]=="0":
                                bookinfo = bookinfo
                        else:
                            file.write( bookinfo[0]+","+ bookinfo[1]+","+ bookinfo[2]+","+ bookinfo[3]+","+ bookinfo[4]+","+ bookinfo[5]+"\n")

                    if borrowedCopies > 0:
                        print("Book cannot be removed: borrowed copies must be 0")
                        file.close()

                    else:
                        print("Book was removed successfully")
                        file.close()

                elif yesOrNo == "n":

                    print("operation is cancelled")
                    file.close()

# function-5
def borrow():                         # this function will allow the user to borrow a book.
    match = 0
    errors = False                     # if an error happens, this  will change to True.
    serialExistence = False            # if a serial number exists in the file this will change to True.
    NewBookList = bookList()
    booksFile = open("booksInfo.txt", "r")
    borrowedfile = open("borrowedInfo.txt", "r")
    serial = input("Enter book serial number to borrow: ")
    if len(serial) != 5:                                        # to check the length of the serial number.
        print("Error: serial number should be 5 digits")
        errors = True

    elif serialExistence == False:
        bookIndex = 0
        for book in NewBookList:        # to get the index of the book we want to borrow from the list.
            if serial in book:
                serialExistence = True
            elif serialExistence != True :
                bookIndex = bookIndex + 1
                serialExistence = False

        if serialExistence == True:
             copies = (NewBookList[bookIndex])      # to check if there is any copies to borrow.
             copies = copies[4]
             if copies == "0":
                print("Error: no available copies in the library")
                errors = True
                serialExistence = False
                match = 1


        if serialExistence == False and match == 0:   # to check if the serial exists in the file.
            print("Error: no matched serial number")
            errors = True

    if serialExistence == True:
        numOfBorrowed = 0
        id = input("Enter user ID: ")
        borrowedInfoList = []
        for line in borrowedfile:                       # to get how many books this person has already borrowed.
            line = line.strip().split(",")
            borrowedInfoList.append(line)
        for book in borrowedInfoList:
            if id in book:
                numOfBorrowed = numOfBorrowed + 1

        if numOfBorrowed >= 3:
            print("Error: user cannot borrow more than 3 books")
            errors = True

        else:
            borrowedfile = open("borrowedInfo.txt", "r")
            numOfcopys = 0
            sameBooklist = []
            for line in borrowedfile:                   # to check if the person borrowed the same book before.
                if id in line and serial in line:
                    print("Error: user already borrowed a copy of the book")
                    errors = True


    if errors == False:
        linePostion = 0
        found = False
        for book in NewBookList :
            if serial in book[0] and found != True: # to get the number of copies and borrowed books.
                linePostion = linePostion
                found = True
            elif found == False:
                linePostion = linePostion + 1

        NewBookList[linePostion][4] = str(int(NewBookList[linePostion][4]) - 1) # decreasing the number of copies by 1
        NewBookList[linePostion][5] = str(int(NewBookList[linePostion][5]) + 1) # increasing the number of copies by 1
        booksFile = open("booksInfo.txt", "w")
        for bookinfo in NewBookList:
            booksFile.write( bookinfo[0]+","+ bookinfo[1]+","+ bookinfo[2]+","+ bookinfo[3]+","+ bookinfo[4]+","+ bookinfo[5]+"\n")

        borrowedfile = open("borrowedInfo.txt", "r")
        borrowedInfoList = []
        for line in borrowedfile:
            line = line.strip().split(",")
            borrowedInfoList.append(line)
        newBorrow = [serial,id]
        borrowedInfoList.append(newBorrow)
        borrowedfile = open("borrowedInfo.txt", "w")
        for borrowedInfo in borrowedInfoList:
            borrowedfile.write(borrowedInfo[0]+","+ borrowedInfo[1]+"\n")

        print("Book was borrowed successfully")

    booksFile.close()
    borrowedfile.close()

# function-6
def Return():                         # this function will return a borrowed copy to the file.
    serialNumber = input("Enter book serial number to return: ")
    ID = input("Enter user ID: ")
    borrowFile = open("borrowedInfo.txt","r")
    bookCounter = 0
    serialCounter = 0
    borrowv = False
    borrowedInfoList = []                    # making a list for the borrowed file.
    for line in borrowFile:
        line = line.strip().split(",")
        borrowedInfoList.append(line)
    borrowFile = open("borrowedInfo.txt","w")
    for book in borrowedInfoList:
        if serialNumber in book[0] and ID in book[1]: #  checking if the entered information match any information in the list
            serialNumber = serialNumber               ## then removing it from the file.
            borrowv = True
        else:
            borrowFile.write(book[0]+","+book[1]+"\n")


    if borrowv == True:
        NewBookList = bookList()                      #  geting the index of the book in the "booksInfo" file to change the
        linePostion = 0                               ## number of copies and borrowed book.
        found = False
        booksFile = open("booksInfo.txt", "w")
        for book in NewBookList :
            if serialNumber in book[0] and found != True:
                linePostion = linePostion
                found = True
            elif found == False:
                linePostion = linePostion + 1

        NewBookList[linePostion][4] = str(int(NewBookList[linePostion][4]) + 1) # increasing the number of copies by 1
        NewBookList[linePostion][5] = str(int(NewBookList[linePostion][5]) - 1) # decreasing the number of borrowed by 1
        for bookinfo in NewBookList:
            booksFile.write( bookinfo[0]+","+ bookinfo[1]+","+ bookinfo[2]+","+ bookinfo[3]+","+ bookinfo[4]+","+ bookinfo[5]+"\n")
        booksFile.close()
    if borrowv == True:
        print("Book was returned successfully")
    else:
        print("Error: no matched record found in borrowedInfo.txt")




    borrowFile.close()

# main program
def main():                           # this function will run the program.
    RUN = True
    while RUN == True:
        choice = menu()
        if choice == "1":
            PrintBooksInfo()
        elif choice == "2":
            if search() == False:                  # to print "there are no matched books" if 0 books was found.
                print("No matched record found")
        elif choice == "3":
            addBook()
        elif choice == "4":
            RemoveBook()
        elif choice == "5":
            borrow()
        elif choice == "6":
            Return()
        elif choice == "7":
            RUN = False
        else:
            print("Invalid Menu Option")

main()
