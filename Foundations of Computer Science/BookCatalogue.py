#BELOTINDOS, JOHN RAFAEL P.
#G-1L
#This code organizes my books, it serves as my personal book catalogue. It keeps track of the book code, book name, author, price, date bought, status and notes.
BOOKS = {} #This is the main dictionary
BOOKNOTES={} #This is a seperate dictionary only for notes

def clearLibrary(): #This block of code clears the library
    print("No more books in your catalogue :(")
    print()
    BOOKS.clear()
    BOOKNOTES.clear()
    main()

def removeBook(): #This block of code removes a specific book from the library
    print("====== REMOVE BOOK ======","\nEnter code of book to remove it from the library:")
    bookcodecopy = list(BOOKS.keys())
    bookcodefind = input()
    if bookcodefind in bookcodecopy:
        print ("Deleted",BOOKS[bookcodefind]["Book name"],"by",BOOKS[bookcodefind]["Author"]+".")
        del BOOKS[bookcodefind]
        del BOOKNOTES[bookcodefind]
        print("========================","\n")
    else:
        print("Book code does not exist.")  
        print("========================","\n")        
    main()

def addNote(): #This block of code adds a note to a specific book
    print("======= ADD NOTE =======")
    print("Enter a code of a book to add a note to it.")
    bookcodecopy = list(BOOKNOTES.keys())
    bookcodefind = input()
    if bookcodefind in bookcodecopy:
        print("Add a note to",BOOKS[bookcodefind]["Book name"],"by",BOOKS[bookcodefind]["Author"]+":",end="")
        note=input()
        BOOKNOTES[bookcodefind].append(note)  #from https://www.geeksforgeeks.org/python/appending-to-list-in-python-dictionary/ this code appends to a list that is inside a dictionary
        print("Added note. :)")
        print("========================")
        print()
    else:
        print("Book code does not exist.")  
        print("========================")   
        print()     
    main()

def changeStatus(): #This block of code changes the status of a specific book
    print("===== CHANGE STATUS =====")
    print("Enter code to change its status:")
    bookcodecopy = list(BOOKS.keys())
    bookcodefind = input()
    if bookcodefind in bookcodecopy:
        print("New status of", BOOKS[bookcodefind]["Book name"],"by",BOOKS[bookcodefind]["Author"]+":")
        while True:
            newstat=input()
            if newstat in statuses:
                BOOKS[bookcodefind]["Status"]=newstat
                print("Status changed!")
                print("========================","\n")
                break
            else: 
                print("Status can only be to-read, currently-reading, finished")
    else:
        print("Book code does not exist.")  
        print("========================")   
        print()     
    main()

def viewCatalogue(): #This block of code shows all the books in the library
    print("======","MY LIBRARY","======")
    if BOOKS=={}:
        print("Your library is empty. Add some books!")
        print("========================\n")
        main()
    else:
        for key,value in list(BOOKS.items()):
            print()
            print (key)
            for i,j in list(value.items()):
                print(i+":",j)
            print("My notes:")
            if BOOKNOTES[key]==[]:
                print("\tNo notes yet...")
            else:
                for p in BOOKNOTES[key]:
                    print("\t> ",p)
    print()
    print("========================\n")
    main()

statuses = ["to-read","currently-reading","finished"]
def addBook(): #This block of code adds a book to your library
    print("====== ADD A BOOK ======")
    bookcode = input("Book code: ")
    bookname =  input("Book name: ")
    author =  input("Author: ")
    price = float(input("Price: "))
    datebought = input("Date bought: ")
    while True:
        status=input("Status: ")
        if status in statuses:
            break
        else: 
            print("Status can only be to-read, currently-reading, finished")
    BOOKS[bookcode]={"Book name":bookname,
                     "Author":author,
                     "Price":price,
                     "Date bought":datebought,
                     "Status":status}
    BOOKNOTES[bookcode]=[]
    print("Book added!")
    print("========================\n")
    main()

def main(): #This is the main menu.
    print("=========","MENU","=========")
    print("[1] Add a Book")
    print("[2] View All Books")
    print("[3] Change Book Status")
    print("[4] Add Note to Book")
    print("[5] Remove Book")
    print("[6] Clear Book Catalogue")
    print("[0] Exit")
    print("========================")
    option = int(input("Enter option:"))
    print()
    if option>6 or option<0:
        print("Options are only from 0 to 6\n")
        main()
    elif option==1:
        addBook()
    elif option==2:
        viewCatalogue()
    elif option==3:
        changeStatus()
    elif option==4:
        addNote()
    elif option==5:
        removeBook()
    elif option==6:
        clearLibrary()
    elif option==0:
        print()
main()
