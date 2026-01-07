#BELOTINDOS, JOHN RAFAEL P.
#G-1L
#This code organizes my books, it serves as my personal book catalogue. It keeps track of the book code, book name, author, price, date bought, status and notes. It now also saves and loads data to and from books.dat.
BOOKS = {} #This is the main dictionary
BOOKNOTES={} #This is a seperate dictionary only for notes

import belotindos_saveload #This code imports functions from belotindos_saveload.py

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
        print("Add a note to",BOOKS[bookcodefind]["Book name"],"by",BOOKS[bookcodefind]["Author"]+": ",end="")
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
    print("[3] Save Catalogue")
    print("[4] Load Catalogue")
    print("[5] Change Book Status")
    print("[6] Add Note to Book")
    print("[7] Remove Book")
    print("[8] Clear Book Catalogue")
    print("[0] Exit")
    print("========================")
    option = int(input("Enter option:"))
    print()
    if option>8 or option<0:
        print("Options are only from 0 to 6\n")
        main()
    elif option==1:
        addBook()
    elif option==2:
        viewCatalogue()
    elif option==5:
        changeStatus()
    elif option==6:
        addNote()
    elif option==7:
        removeBook()
    elif option==8:
        clearLibrary()
    elif option==0:
        print()
    elif option==3:
        print("====== SAVING BOOKS TO books.dat ======")
        for key,value in BOOKS.items():
            print("Added",key,"("+BOOKS[key]["Book name"],BOOKS[key]["Author"]+")","to books.dat" )
        print("Successfully saved the book catalogue!!","\n=======================================\n")
        belotindos_saveload.saveCatalogue(BOOKS,BOOKNOTES)
        main()
    elif option==4:
        belotindos_saveload.loadCatalogue(BOOKS,BOOKNOTES)
        print("====== LOADING BOOKS FROM books.dat ======","\nSuccessfully loaded the book catalogue containing:")
        for key,value in BOOKS.items():
            print(key,"("+BOOKS[key]["Book name"],BOOKS[key]["Author"]+")")
        print("==========================================\n")
        main()
main()
