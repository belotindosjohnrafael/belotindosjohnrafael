#Belotindos, John Rafael P.
#G-1L
#This code loops infinitely until user types zero or it does two things, (1) prints from n to n^2, in an nxn pattern. and (2) creates a password verification system that checks if the password is valid.

#MAIN MENU
while True:
    print ("Welcome to this menu! If you think this works, you already have done half the battle!\n(1) Do part 1\n(2) Do Part 2\n(0) Exit application\n" )
    choice = int(input("Enter your choice: "))

    #MENU 1
    if choice == 1: 
        print ("This is a for loop that prints from n to n^2, in an nxn pattern.")
        n = int(input("Enter a number: "))
        squared = n**2
        for i in range(1,squared+1):
            space = int(len(str(squared))) - int(len(str(i))) #from programiz.com/python-programming/examples/number-of-digits -  This code counts the number of digits of squared and i then subtracts it to identify how many spaces to use for proper alignment.
            print (" "*n,i, end=" "*space)
            if i%n == 0: # this determines where to enter a new line
                print ("\n")
    #MENU 2
    elif choice == 2:
        password = input("Enter your password here!")  
        login = input("Please login your password here. ")
        while login != password:
            print("Incorrect password!")
            login = input("Please try again. ")
        print ("Successful login!")
    #EXIT
    elif choice == 0:
        print ("Exited successfully.")
        break
    #INVALID
    else: 
        print ("You have entered an invalid number.")