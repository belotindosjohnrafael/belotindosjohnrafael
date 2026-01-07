#BELOTINDOS, JOHN RAFAEL P.
#G-1L
#This program are sets of definitions that are being imported by belotindos_ex7.py to save or load book catalogues.
def saveCatalogue(BOOKS,BOOKNOTES): #This block of code saves the books to books.dat
    file = open("books.dat","w")
    for key,value in list(BOOKS.items()): #This loop gets the key and value on the main disctionary
        subtyper = [] #These sublists empty out every iteration
        subnoter = []
        subtyper.append(key)
        for a,b in list(value.items()): #This loop gets the key and value of sub dictionary.
            c=str(b)
            subtyper.append(c)
        for p in BOOKNOTES[key]:
            subnoter.append(p)
        notesjoiner = "|".join(subnoter)
        joiner = "|".join(subtyper) #This code converts the list into one string.
        file.write(str(joiner)+"\n")
        file.write(str(notesjoiner)+"\n")
    
    file.close()

def loadCatalogue(BOOKS,BOOKNOTES): #This block of code loads books.dat to belotindos_ex7.py
    file=open("books.dat","r")
    organizer = 1 #This code is the determinator if we are on Book Info or Book Notes
    currentcode = "placeholder" #Local bookcode to loadCatalogue so elif organizer==2 can access it
    for line in file: 
        if organizer==1:
            lister = line[:-1] #This removes \n
            listofunloaded = list(lister.split("|")) #This code splits the one string to lists
            organizer+=1
            bookcode = listofunloaded[0]
            currentcode=bookcode
            bookname =  listofunloaded[1]
            author =  listofunloaded[2]
            price = float(listofunloaded[3])
            datebought = listofunloaded[4]
            status=listofunloaded[5]
            BOOKS[bookcode]={"Book name":bookname,
                     "Author":author,
                     "Price":price,
                     "Date bought":datebought,
                     "Status":status}
            BOOKNOTES[bookcode]=[]
            
        elif organizer==2: #This code organizes the notes in books.dat to be appended again to Booknotes.
            noter = line[:-1]
            sepnote = list(noter.split("|"))
            organizer-=1
            if sepnote == ['']:
                None
            else:
                for i in range(len(sepnote)):
                    BOOKNOTES[currentcode].append(sepnote[i])
    file.close()
    return BOOKS,BOOKNOTES    
    