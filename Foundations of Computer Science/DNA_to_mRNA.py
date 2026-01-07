#BELOTINDOS, JOHN RAFAEL P.
#G-1L
#This program transcribes a list of DNA sequences to mRNA and translates the resulting mRNA strands to its protein sequences.

#STORAGE
Phe = ["UUU","UUC"]
Leu = ["UUA","UUG","CUU","CUC","CUA","CUG"]
Ile = ["AUU","AUC","AUA"]
Val = ["GUU","GUC","GUA","GUG"]
Ser = ["UCU","UCC","UCA","UCG"]
Pro = ["CCU","CCC","CCA","CCG","AGU","AGC"]
Thr = ["ACU","ACC","ACA","ACG"]
Ala = ["GCU","GCC","GCA","GCG"]
Tyr = ["UAU","UAC"]
His = ["CAU","CAC"]
Gln = ["CAA","CAG"]
Asn = ["AAU","AAC"]
Lys = ["AAA","AAG"]
Asp = ["GAU","GAC"]
Glu = ["GAA","GAG"]
Cys = ["UGU","UGC"]
Trp = ["UGG"]
Arg = ["CGU","CGC","CGA","CGG","AGA","AGG"]
Gly = ["GGU","GGC","GGA","GGG"]
stop = ["UAA","UAG","UGA"]
mainlistofDNA = []
mainlistofRNA = []
mainlistofProtein = []

def processed_data(): #This block shows the user all the processed data.
    if mainlistofDNA == []:
        print("No list of DNA sequences yet.")
        main()
    print("--- View all processed data ---")
    for p in range (len(mainlistofDNA)):
        print("[ SEQUENCE", p+1,"]")
        print("DNA:",mainlistofDNA[p])
        if mainlistofRNA!=[]:
            print("RNA:",mainlistofRNA[p])
        if mainlistofProtein!=[]:
            print("Protein:",mainlistofProtein[p])
    main()

def translate_to_protein(): #This function converts the mRNA to its protein sequence.
    if mainlistofDNA == []:
        print("No list of DNA sequences yet.")
        main()
    if mainlistofRNA==[]:
        print("Transcription to mRNA was not done yet.")
        main()
    for o in range(len(mainlistofRNA)):
        seperate = mainlistofRNA[o]
        p=3
        l=0
        f=False
        subllistofProtein = []
        for d in range(int(int(len(seperate))/3)):
            combination = seperate[l:p]
            p+=3
            l+=3
            if combination == "AUG":
                subllistofProtein.append("Met")
                f=True
            if f is True:
                if combination in Phe:
                    subllistofProtein.append("Phe")
                elif combination in Leu:
                    subllistofProtein.append("Leu")
                elif combination in Ile:
                    subllistofProtein.append("Ile")
                elif combination in Val:
                    subllistofProtein.append("Val")
                elif combination in Ser:
                    subllistofProtein.append("Ser")
                elif combination in Pro :
                    subllistofProtein.append("Pro")
                elif combination in Thr:
                    subllistofProtein.append("Thr")
                elif combination in Ala :
                    subllistofProtein.append("Ala")
                elif combination in Tyr :
                    subllistofProtein.append("Tyr")
                elif combination in His :
                    subllistofProtein.append("His")
                elif combination in Gln :
                    subllistofProtein.append("Gln")
                elif combination in Asn :
                    subllistofProtein.append("Asn")
                elif combination in Lys :
                    subllistofProtein.append("Lys")
                elif combination in Asp:
                    subllistofProtein.append("Asp")
                elif combination in Glu :
                    subllistofProtein.append("Glu")
                elif combination in Cys :
                    subllistofProtein.append("Cys")
                elif combination in Trp:
                    subllistofProtein.append("Trp")
                elif combination in Arg :
                    subllistofProtein.append("Arg")
                elif combination in Gly :
                    subllistofProtein.append("Gly")
                elif combination in stop :
                    break
        joiner ='-'.join(subllistofProtein)
        mainlistofProtein.append(joiner)
        print("[ SEQUENCE", o+1,"]")
        print(mainlistofProtein[o])   
    print("Transcription complete.")
    main()

def transcribe_to_rna(): #This function converts the DNA sequences to RNA.
    if mainlistofDNA == []:
        print("No list of DNA sequences yet.")
        main()
    else: 
        for i in range(len(mainlistofDNA)):
            seperator = mainlistofDNA[i]
            sublistofRNA = []
            converted=seperator
            for j in range(len(seperator)): #I used nested loops to break down the list of DNA Sequence
                stringseperate=seperator[j]
                if stringseperate=="A":
                    converted = stringseperate.replace("A","U")
                elif stringseperate=="T":
                    converted = stringseperate.replace("T","A")
                elif stringseperate=="C":
                    converted = stringseperate.replace("C","G")
                elif stringseperate=="G":
                    converted = stringseperate.replace("G","C")
                sublistofRNA.append(converted)
            joiner =''.join(sublistofRNA)       #from https://www.geeksforgeeks.org/python/python-program-to-convert-a-list-to-string/ - This code converts the list sublistofRNA to strings to be appended as one item to the mainlistofRNA.
            mainlistofRNA.append(joiner) 
            print("[ SEQUENCE", i+1,"]")
            print(mainlistofRNA[i])
        print("Transcription complete.")
    main()      
                
def input_data():  #This function is where we input the list of DNA sequences.
    num_of_sequences = int(input("How many sequences do you want to input? "))
    if num_of_sequences > 5-int(len(mainlistofDNA)) or num_of_sequences <1:
        print("Error: should input minimum of 1 sequence and maximum of 5 sequences.")
        main()
    else:
        for i in range (num_of_sequences):
            DNA = input("Enter Sequence "+str((i+1))+":")
            if int(len(DNA))<6 or int(len(DNA))>21:
                print ("Each DNA sequence shall only have a minimum length of 6 and maximum of 21.")
                mainlistofDNA.clear
                main()
            else :
                mainlistofDNA.append(DNA)
    main()

def main():
    print("========================================")
    print("[1] Enter list of DNA sequences")
    print("[2] Transcribe to mRNA")
    print("[3] Translate to protein sequences")
    print("[4] View all processed data")
    print("[0] Exit")
    chooser = int(input("Enter choice: "))
    if chooser==1:
        input_data()
    if chooser==2:
        transcribe_to_rna()
    if chooser==3:
        translate_to_protein()
    if chooser==4:
        processed_data()
    if chooser==0:
        exit()
        
main()

def exit():
    []
