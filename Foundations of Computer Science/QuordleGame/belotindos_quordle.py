#BELOTINDOS, JOHN RAFAEL P.
#Section: G-1L
#Final Project
#This is QUORDLE where a player is given nine tries to guess 4 words.

import random
import time
#COLORS
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

wordlist=[] #This is list for the words that is already used in the word randomizer, to prevent doubling of words.
guessedlist =[] #This list is for the words that the user already guessed. This is used to prevent the user from entering the word again.

rightwords = {"set1": [], #This dictionarycontains the right words that needs to be guessed.
              "set2": [],
              "set3": [],
              "set4": []}

randomword ="" #This is just the current random word that the loop gets in randomcheck().
word_bank = open("word_bank.txt","r").read().splitlines()

userguess = {"set1": [], #This dictionary contains the user guess that are not yet checked.
              "set2": [],
              "set3": [],
              "set4": []}

checkedwords = {"set1": [], #This dictionary contains the user guess with the colors.
              "set2": [],
              "set3": [],
              "set4": []}

pastprints = {"set1": [],#This dictionary contains all the user gues in each quadrant even the past one .
              "set2": [],
              "set3": [],
              "set4": []}

thequadrupler = {"layer1": [],# This dictionary containes the layers used for printing the board
              "layer2": []}

state = {"set1": [], #This entails the state of the quadrant 1st state - shown word | 2nd state hidden.
              "set2": [],
              "set3": [],
              "set4": []}

lives = 1 #This is the lives of the player(reverse because I also use it for the guess number.)

scores= {"set1": [0], #This entails the scores the use got per board.
              "set2": [0],
              "set3": [0],
              "set4": [0]}

scorings=1

characterdata = [] #This dictionary is the infos of the current player
name=""

start=0.0 #This is for time
end = 0.0

leaderboard1=[] #This is the list for the leaderboard

def thegreatreset():#before going back to the main menu. It goes here. It resets every list and dictionary and variable used in the code.
    global start
    global end
    global scorings
    global lives
    global randomword
    start=0.0
    end=0.0
    characterdata.clear()
    scorings=1
    for key in scores:
        scores[key]=[0]
    lives=1
    for key in state:
        state[key].clear()
    for key in thequadrupler:
        thequadrupler[key].clear()
    for key in pastprints:
        pastprints[key].clear()
    for key in checkedwords:
        checkedwords[key].clear()
    for key in userguess:
        userguess[key].clear()
    for key in rightwords:
        rightwords[key].clear()
    randomword=""
    guessedlist.clear()
    leaderboard1.clear()
    wordlist.clear()

    main()

def thegreatetcher(): #This saves the leaderboard in leaderboards.txt
    file=open("leaderboards.txt","w")
    for i in range (int(len(leaderboard1))):
        convertedtostr=[]
        for p in range(int(len(leaderboard1[i]))):
            convertedtostr.append(str(leaderboard1[i][p]))
        joiner="|".join(convertedtostr)
        file.write(joiner+"\n")
    file.close()
    thegreatreset()

def userscore():#This prints the score of the player.
        scoresconate=" ".join(str(characterdata[i]) for i in range(1, 5))
        print(r"""                                         
            ▄▄ ▄▄  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄     ▄▄▄▄  ▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄▄             
▀▀▀▀▀ ▀▀▀▀▀ ▀███▀ ██▀██ ██ ██ ██▄█▄   ███▄▄ ██▀▀▀ ██▀██ ██▄█▄ ██▄▄  ▀▀▀▀▀ ▀▀▀▀▀ 
▀▀▀▀▀ ▀▀▀▀▀   █   ▀███▀ ▀███▀ ██ ██   ▄▄██▀ ▀████ ▀███▀ ██ ██ ██▄▄▄ ▀▀▀▀▀ ▀▀▀▀▀ """)
        print()
        print(f'{"NAME":<10} | {"GUESSES":<10} | {"TIME":<10}')
        print(f'{name:<10} | {scoresconate:<10} | {str(characterdata[5])+"s":<10}')
        print("\n")

def leaderboard(): #This prints the leaderboard in the right format
    print(r"""                                                        
            ▄▄    ▄▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄   ▄▄▄   ▄▄▄  ▄▄▄▄  ▄▄▄▄              
▀▀▀▀▀ ▀▀▀▀▀ ██    ██▄▄  ██▀██ ██▀██ ██▄▄  ██▄█▄ ██▄██ ██▀██ ██▀██ ██▄█▄ ██▀██ ▀▀▀▀▀ ▀▀▀▀▀ 
▀▀▀▀▀ ▀▀▀▀▀ ██▄▄▄ ██▄▄▄ ██▀██ ████▀ ██▄▄▄ ██ ██ ██▄█▀ ▀███▀ ██▀██ ██ ██ ████▀ ▀▀▀▀▀ ▀▀▀▀▀  """)
    print()
    print(f'{"NAME":<10} | {"GUESSES":<10} | {"TIME":<10}')
    for i in range (int(len(leaderboard1))):
        scoresconate=" ".join(str(leaderboard1[i][p]) for p in range(1, 5))
        print(f'{leaderboard1[i][0]:<10} | {scoresconate:<10} | {str(leaderboard1[i][5])+"s":<10}')
    print()
    input("Press [Enter] to go back to the main menu")
    thegreatetcher()

def qualified(): #- This code changes the last placer in the leaderboard to the current player, then runs the leaderboard organizer.
    print("You have qualified for the leaderboard! Check your score [1] or go back to the menu [0]")
    print("[1] Check Leaderboard")
    print("[0] Back to Menu")
    for i in characterdata:
        if i==name:  
            leaderboard1[4]=[name]
        else:
            leaderboard1[4].append(str(i))
    leaderboard_organizer()

def qualifying(): #This identifies if the user is qualified for the leaderboards.
    if int(characterdata[6])==int(leaderboard1[4][6]):
        if float(characterdata[5])<float(leaderboard1[4][5]):
            qualified()
        else:
            print("However, you have not been qualified for the leaderboard. Check your score [1] or go back to the menu [0]")
            print("[1] Check Leaderboard")
            print("[0] Back to Menu")
    elif int(characterdata[6])<int(leaderboard1[4][6]):
        qualified()
    else: 
        print("However, you have not been qualified for the leaderboard. Check your score [1] or go back to the menu [0]")
        print("[1] Check Leaderboard")
        print("[0] Back to Menu")

    select = int(input("Input: "))
    
    if select==1:
        userscore()
        leaderboard()
    if select==0:
        thegreatetcher()

def leaderboard_organizer(): #This organizes the leaderboard
    for i in range(len(leaderboard1)):
        for j in range (len(leaderboard1)):
            if int(leaderboard1[i][6])==int(leaderboard1[j][6]):
                if float(leaderboard1[i][5])<float(leaderboard1[j][5]):
                    temp=leaderboard1[i]
                    leaderboard1[i]=leaderboard1[j]
                    leaderboard1[j]=temp
            if int(leaderboard1[i][6])<int(leaderboard1[j][6]):
                temp=leaderboard1[i]
                leaderboard1[i]=leaderboard1[j]
                leaderboard1[j]=temp

def loadleaderboard(): #This loads the leaderboard
    file=open("leaderboards.txt","r")
    for line in file:
        lister = line[:-1]
        listofunloaded = list(lister.split("|"))
        leaderboard1.append([listofunloaded[0], listofunloaded[1], listofunloaded[2], listofunloaded[3], listofunloaded[4], listofunloaded[5], listofunloaded[6]])
    file.close()
    leaderboard_organizer()

def appendtocharac():#This appends the datas to the characterdata list
    global start
    global end
    global name
    end=time.time()
    draftscore=[]
    totalscore=0
    for key in scores:
        draftscore.append(int(scores[key][0]))
        totalscore+=int(scores[key][0])
    draftscore.sort()
    for i in draftscore:
        characterdata.append(i)
    characterdata.append(round(end-start,2))
    characterdata.append(totalscore)
    totalscore=0

def livenessdetector():#12-This detects the user if they still have lives
    global lives
    if lives==9:
        print("You failed to guess the 4 words in 9 guesses. Check your score [1] or go back to the menu [0]")
        print("[1] Check Leaderboard")
        print("[0] Back to Menu")
        appendtocharac()
        select = int(input("Input: "))
        if select==1:
            userscore()
            leaderboard()
        if select==0:
            thegreatetcher()
    if lives<9:
        lives+=1
        guess()

def winorlose(): #11-This detects if the user have already won or no.
    areyouwinningson=0
    for key in state:
        if int(len(state[key]))>0: #If every list in state has a value. then the user won
            areyouwinningson+=1
    
    if areyouwinningson==4:
        print("Congratulations! You solved all 4 words in",lives,"guesses!")
        appendtocharac()
        qualifying()
        

    else:
        areyouwinningson=0
        livenessdetector()

def scorer(): #10- This gets the score of the board when it is done
    global scorings
    for key in scores:
        if int(len(state[key]))>2: #this is for the board to stop printing when it is already done.
            None
        if int(len(state[key]))==2: 
            scores[key][0]=scorings
            state[key].append("scoreinitiated") #This is to show the word for the last time when it is correct(when its all green)
    scorings+=1
    winorlose()

def reset(): #9-This resets the userguess and checkedwords in preperation for the next guess
    for key in userguess:
        userguess[key].clear()
        checkedwords[key].clear()

    for key in thequadrupler:
        thequadrupler[key].clear()

    scorer()
    
    
def printer(): #8- This module is responsible for formating the print statements
    print()
    for key in checkedwords:
        joiner = " ".join(checkedwords[key])

        if int(len(state[key]))==1:
            pastprints[key].append(joiner)
            state[key].append("underlinesinitiated")
        elif int(len(state[key]))>=2:
            pastprints[key].append("         ")
        else:
            pastprints[key].append(joiner)

    thequadrupler["layer1"].append(" Board 1 ")
    thequadrupler["layer1"].append(" Board 2  ")
    thequadrupler["layer2"].append(' Board 3 ')
    thequadrupler["layer2"].append(' Board 4  ')

    for i in range (int(len(pastprints["set1"]))): #-code alternates the word so that it can be printed in a 4x4 format correctly.
        thequadrupler["layer1"].append(pastprints["set1"][i])
        thequadrupler["layer1"].append(pastprints["set2"][i])
        thequadrupler["layer2"].append(pastprints["set3"][i])
        thequadrupler["layer2"].append(pastprints["set4"][i])

    p=0
    for i in thequadrupler["layer1"]:
        if p==0:
            print(i,end=" | ")
            p+=1
        elif p==1:
            print(i)
            p-=1
    print("----------+-----------")
    p=0
    for i in thequadrupler["layer2"]:
        if p==0:
            print(i,end=" | ")
            p+=1
        elif p==1:
            print(i)
            p-=1
    print()
    reset()

def checker(): #7 - This module compares the userguess{} to the rightwords{} then appends the colors to the checkedwords{}.
    for key in rightwords:
        correctnessidentifier = 0
        for i in range (int(len(userguess[key]))):
            if userguess[key][i]==rightwords[key][i]:
                checkedwords[key][i]= GREEN+userguess[key][i]+RESET
                correctnessidentifier+=1
            elif userguess[key][i] in rightwords[key]:
                checkedwords[key][i]= YELLOW+userguess[key][i]+RESET
            else:
                checkedwords[key][i]= RED+userguess[key][i]+RESET
        if correctnessidentifier==5:
            state[key].append("donephase1") #-if 5 words are correct it updates the state of the set.
    printer()

def appender(playerguess): #6 - This module appends the userguess to each set.
    guessedlist.append(playerguess)
    upped = playerguess.upper()
    for key in userguess:
        for letter in upped:
            userguess[key].append(letter)
            checkedwords[key].append(letter) #This acts as a placeholder so that the game wont crash.
    checker()



def guess(): #This module checks the guess of the user if it is appropriate #5
    global start
    what = input('Guess '+str(lives)+":")
    playerguess = what.lower()
    if int(len(playerguess)) != 5:
            print('Your guess must be 5 letters. Try Again.')
            guess()
    if playerguess in word_bank:
        if playerguess in guessedlist:
            print('You guessed that word already. Try again')
            guess()
        appender(playerguess)
    else: 
        print ("Your guess is not in the word bank. Try another.")
        guess()
    
def antirepeat(key): #4 -  This module ensures that there would be no similar words in the set.
        if randomword in wordlist:
            randomcheck(key)
        else:
            wordlist.append(randomword)
            for i in randomword:
                rightwords[key].append(i)

def randomcheck(key): #3
    global randomword
    global word_bank
    randomword = (random.choice(word_bank)).upper() 
    antirepeat(key)

def wordgetter(): #2
    for key in rightwords:#This loop fills up the 4 sets with words.
        randomcheck(key)
    print(wordlist) #C--------------------------------------------show words---------------------------------
    wordlist.clear()
    guess()

def startgame(): #1 - This code starts the game
    global start
    global name
    loadleaderboard()
    while True:
        name = input("What is your name? ")
        if 0<int(len(name))<11:
            break
        else:
            print("Name must be 1-10 characters only")
            continue
    characterdata.append(name)
    print("Hi,",name,"You have 9 guessees to find all four words. Each guess is a five letter word from your word bank.")
    print(GREEN+"GREEN"+RESET+": Correct letter and position.")
    print(YELLOW+"YEELLOW"+RESET+": Correct letter but wrong position.")
    print(RED+"RED"+RESET+": Incorrect Letter.")
    print()
    start=time.time() #This records the start time
    wordgetter()
#=========== WORD BANK CHECKER MODULE ==========#
def checkwordbank(): #this code prints all the words in the wordbank.
    print()
    print(r"""                                                                          
            ▄▄   ▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄    ▄▄▄▄   ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄             
▀▀▀▀▀ ▀▀▀▀▀ ██ ▄ ██ ██▀██ ██▄█▄ ██▀██   ██▄██ ██▀██ ███▄██ ██▄█▀ ▀▀▀▀▀ ▀▀▀▀▀ 
▀▀▀▀▀ ▀▀▀▀▀  ▀█▀█▀  ▀███▀ ██ ██ ████▀   ██▄█▀ ██▀██ ██ ▀██ ██ ██ ▀▀▀▀▀ ▀▀▀▀▀ """)
    print()
    word_bank = open("word_bank.txt","r")
    organize=0
    for line in word_bank:
        if organize==9:
            print(line[:-1])
            organize=0
        else:
            print(line[:-1],end="   ")
            organize+=1
    word_bank.close()
    print()
    input("\nPress [Enter] to go back to the main menu")
    main()

def showleads(): #This block of code is for the show leaderboard main menu
    templead=[]
    file=open("leaderboards.txt","r")
    for line in file:
        lister = line[:-1]
        listofunloaded = list(lister.split("|"))
        templead.append([listofunloaded[0], listofunloaded[1], listofunloaded[2], listofunloaded[3], listofunloaded[4], listofunloaded[5], listofunloaded[6]])
    file.close()
    print(r"""                                                                                                                                 
            ▄▄    ▄▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄   ▄▄▄   ▄▄▄  ▄▄▄▄  ▄▄▄▄              
▀▀▀▀▀ ▀▀▀▀▀ ██    ██▄▄  ██▀██ ██▀██ ██▄▄  ██▄█▄ ██▄██ ██▀██ ██▀██ ██▄█▄ ██▀██ ▀▀▀▀▀ ▀▀▀▀▀ 
▀▀▀▀▀ ▀▀▀▀▀ ██▄▄▄ ██▄▄▄ ██▀██ ████▀ ██▄▄▄ ██ ██ ██▄█▀ ▀███▀ ██▀██ ██ ██ ████▀ ▀▀▀▀▀ ▀▀▀▀▀ """)
    print()
    print(f'{"NAME":<10} | {"GUESSES":<10} | {"TIME":<10}')
    for i in range (int(len(templead))):
        scoresconate=" ".join(str(templead[i][p]) for p in range(1, 5))
        print(f'{templead[i][0]:<10} | {scoresconate:<10} | {str(templead[i][5])+"s":<10}')
    print()
    input("Press [Enter] to go back to the main menu")
    templead.clear()
    main()

#Main Module -  This is the main menu
def main():
    print( r"""                          
    ___  ___      ________  ___  ___  ________  ________  ________  ___       _______           ___  ___    
   /  /|/  /|    |\   __  \|\  \|\  \|\   __  \|\   __  \|\   ___ \|\  \     |\  ___ \         |\  \|\  \   
  /  / /  / /    \ \  \|\  \ \  \\\  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \    \ \   __/|        \ \  \ \  \  
 /  / /  / /      \ \  \\\  \ \  \\\  \ \  \\\  \ \   _  _\ \  \ \\ \ \  \    \ \  \_|/__       \ \  \ \  \ 
|\  \/\  \/        \ \  \\\  \ \  \\\  \ \  \\\  \ \  \\  \\ \  \_\\ \ \  \____\ \  \_|\ \       \/  /\/  /|
\ \  \ \  \         \ \_____  \ \_______\ \_______\ \__\\ _\\ \_______\ \_______\ \_______\      /  ///  // 
 \ \__\ \__\         \|___| \__\|_______|\|_______|\|__|\|__|\|_______|\|_______|\|_______|     /_ ///_ //  
  \|__|\|__|               \|__|                                                               |__|/|__|/                                                                                                                                                                                                                                                                                                                                                            
""")
    print("[1] Play Quordle!")
    print("[2] Check Word Bank")
    print("[3] See Leaderboard")
    print("[0] Exit\n")
    choice = int(input("Choice: "))
    if choice==1:
        startgame()
    if choice==2:
        checkwordbank()
    if choice==3:
        showleads()
    if choice==0:
        exit()
main()
