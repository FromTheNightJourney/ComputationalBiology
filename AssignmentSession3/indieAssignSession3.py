# InputDNA = "TTACGA"
# Complement = AATGCT
# mRNA = AAUGCU
# Amino Acid = Asn (N) - Ala (A)
# Input should be multiples of 3.

from tempCodonTable import codonTab

# Assuming codontab is imported from tempCodonTable
# codontab is a dictionary mapping codons to amino acids

def translatingOne(userInput):
    dnaSeq = userInput.upper()
    
    print('InputDNA = "' + dnaSeq + '"')
    
    if len(dnaSeq) % 3 != 0:
        print("Your DNA string is not divisible by 3.\n")
        return False  # Exit the function when the length is not divisible by 3
    
    # validation
    valid = dnaSeq.count("A") + dnaSeq.count("C") + dnaSeq.count("T") + dnaSeq.count("G")
    if valid == len(dnaSeq):
        pass
    else:
        print("Entered DNA is invalid.\n")
        return
    
    # complement maker
    comp = []
    complementDict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in dnaSeq:
        comp.append(complementDict[i])
    compdata = ''.join(comp)
    print("Complement = " + compdata)

    # mRNA maker
    mRNA = ""
    for i in compdata:
        if i != "T":
            mRNA = mRNA + i
        else:
            mRNA = mRNA + "U"
    print("mRNA = " + mRNA)

    # protein maker
    proteinList, varCounter, tempProteinList, tempFinalProtein, proteinString, stringcounterFormat = [], 0, [], [], "", 0
    
    for i in mRNA:
        tempProteinList.append(i)
        varCounter += 1
        if varCounter == 3:
            tempProteinString = ''.join(tempProteinList).upper()
            proteinEquivalent = codonTab.get(tempProteinString)
            if proteinEquivalent:
                tempFinalProtein.append(proteinEquivalent)
            tempProteinList = []
            varCounter = 0
            
    dumCounter = 0
    for i in tempFinalProtein:
        if stringcounterFormat == 0:
            proteinString = proteinString + i
            stringcounterFormat += 1
        else:
            proteinString = proteinString + " - " + i
            stringcounterFormat +=1
        

    print("Amino Acid = ", proteinString)
    return True

while True:
    userInput = input("Please enter a DNA sequence: ")
    if translatingOne(userInput):
        break
