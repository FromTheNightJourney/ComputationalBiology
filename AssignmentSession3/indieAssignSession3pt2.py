# Input Amino Acid = WYW

# mRNA = UGGUACUUGG
# UGG = 2
# UAC = 1

# mRNA = UGGUAUUGG
# UGG = 2
# UAU = 1

# keys = [k for k, v in d.items() if v == 'aaa']
# print(keys)
# ['key1', 'key2']
from tempCodonTable import simplecodontab
import itertools
from collections import Counter

def checkValidAmino(userInput):
    tempCodon = []

    aminoAcid = list(userInput.upper())
    print("Inputted Amino Acid = ", userInput.upper())
    
    if len(aminoAcid) > 3 or len(aminoAcid) < 1:
        print("Invalid input length. Please try again.")
        return None
    else:
        for i in aminoAcid:
            keys = [x for x, v in simplecodontab.items() if v == i]
            if not keys:
                print("Invalid letter inputted. Please try again.")
                return
            else:
                tempCodon.append(keys)
        allCodons = [''.join(x) for x in itertools.product(*tempCodon)]
        return allCodons

def reversedAminoAcid(userInput):
    result = checkValidAmino(userInput)
    if result:
        print("Possible mRNA sequences:")
        for r in result:
            print(r)
        for r in result:
            codon_count = Counter([r[i:i+3] for i in range(0, len(r), 3)])
            print(f"\nmRNA = {r}")
            for codon, count in codon_count.items():
                print(f"{codon} = {count}")
        return True
    return False


while True:
    userInput = input("Input the Amino Acid you want to convert: ")
    if reversedAminoAcid(userInput):
        break
    
# self notes:
# itertools compute cartesian product of input iterables, allowing all combinations of list  
# [['xxx'], ['yyy', 'www'], ['zzz']] = ['xxxyyyzzz', 'xxxwwwzzz']
# that is where the code leaves off by the way ^_^