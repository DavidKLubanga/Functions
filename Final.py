#DAVID LUBANGA
#EXAM II
#05-10-2023


import re
import os


#1

import os
import re

file = input("What file would you like to analyze? ")
readFile = open(file)
fasta = readFile.read()

#print(fasta)
#print(len(fasta))

exon1 = fasta[0:62]
intron = fasta[63:90]
exon2 = fasta[91:125]

newFile1 = open("coding.txt", "w")
newFile1.write(intron)
newFile1.close()

newFile2 = open("non_coding.txt", "w")
newFile2.write(exon1)
newFile2.write("\n")
newFile2.write(exon2)
newFile2.close()


#2


intronLen = len(intron)
combinedExons = len(exon1 + exon2)
print("The sequence has a coding percentage of: ", str((intronLen/combinedExons)*100), "%")


#3

import os
import re

file1 = open("Q2_AccessionNumbers.txt", "r")
accession = file1.read()
numbers = accession.split("\n")
#print(numbers)

file2 = open("Q2_sequences.txt", "r")
dna = file2.read()
uppDNA = dna.replace("-", "").upper()
seq = uppDNA.split("\n")


newFasta1 = open(numbers[0] + ".txt", "w")
newFasta1.write(">")
newFasta1.write(numbers[0])
newFasta1.write("\n")
newFasta1.write(seq[0])

newFasta1.close()

newFasta2 = open(numbers[1] + ".txt", "w")
newFasta2.write(">")
newFasta2.write(numbers[1])
newFasta2.write("\n")
newFasta2.write(seq[1])

newFasta2.close()

newFasta3 = open(numbers[2] + ".txt", "w")
newFasta3.write(">")
newFasta3.write(numbers[2])
newFasta3.write("\n")
newFasta3.write(seq[2])

newFasta3.close()

#Loop to work with more FASTA sequences...
#for x in range(len(numbers)):
    #filename = numbers[x] + ".txt"
    #newFasta = open(filename, "w")
    #newFasta.write(">")
    #newFasta.write(numbers[x])
    #newFasta.write("\n")
    #newFasta.write(seq[x])
    #newFasta.close()


#4


userSeq1 = input("What is your first DNA sequence? (Please enter only 'A', 'T', 'G', or 'C'")
userSeq2 = input("What is your second DNA sequence? (Please enter only 'A', 'T', 'G', or 'C'")

comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
userSeq3 = ''.join([comp[nuc] for nuc in reversed(userSeq2)])
if userSeq3 == userSeq1:
    print("The given sequences are reverse complements")
else:
    print("The given sequences are NOT reverse complements")


#5


organisms = int(input("What is the starting number of organisms? (2 or more) "))
while organisms < 2:
    organisms = int(input("What is the starting number of organisms? (2 or more) "))

avgInc = int(input("What is the average daily population increace as a percentage? (Positive #) "))
while avgInc < 0:
    avgInc = int(input("What is the average daily population increace as a percentage? (Positive #) "))

days = int(input("How many days will they multiply for? (1 or more) "))
while days < 1:
    days = int(input("How many days will they multiply for? (1 or more) "))


#avgInc2 = avgInc/100
#o = organisms*(avgInc2)
#print(o)

print("Day          Organisms")
print("----------------------")
print("1           ", organisms)


for day in range(2, days + 1):
    popSize = organisms * (1 + avgInc/100) ** (day - 1)
    print(day, "          ", popSize)


#6

import os
import re

inputs = []
array = ""
countr = 0
while array != "quit":
    array = input("Please enter a line followed by enter. Exit by typing 'quit': ")
    if array != "quit":
        inputs.append(array)
        countr = countr + 1

print("You entered", countr, "lines")

#inputs.sort()
#print("Your inputs sorted in ascending order: ")
#for line in inputs:
#    print(line)

for output in range(1, 4):
    print(inputs[output])


#7


#See question 6 above. The sorting code is commented out above.



#8


sequences = input("Please enter your sequence lengths seperated by spaces (ex. 100 123 45 ...etc. ")
seqArray = sequences.split(" ")
numbers  = [int(numbers) for numbers in seqArray]

for value in numbers:
    sums = sum(numbers)
print(sums)
print(sums/len(numbers))



#9

import os
import re

def dna_Comp(fasta):
    numA = re.findall(r"A", fasta)
    numT = re.findall(r"T", fasta)
    numG = re.findall(r"G", fasta)
    numC = re.findall(r"C", fasta)
    numN = len(fasta) - len(numA) - len(numT) - len(numG) - len(numC)
    print("There are", len(numA), "A nucleotides")
    print("There are", len(numT), "T nucleotides")
    print("There are", len(numG), "G nucleotides")
    print("There are", len(numC), "C nucleotides")
    print("There are", numN, "N (unknown) nucleotides")

def at_Comp(fasta):
    numA = re.findall(r"A", fasta)
    numT = re.findall(r"T", fasta)
    numAT = len(numA) + len(numT)
    print((numAT / len(fasta)) * 100)

def gc_Comp(fasta):
    numG = re.findall(r"G", fasta)
    numC = re.findall(r"C", fasta)
    numGC = len(numG) + len(numC)
    print((numGC / len(fasta)) * 100)

def compliment(fasta):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp2 = ''.join([comp[nuc] for nuc in fasta])
    print(comp2)

def reverse_Compliment(fasta):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp2 = ''.join([comp[nuc] for nuc in reversed(fasta)])
    print(comp2)

def mother_function():
    prompt1 = input("Please enter the file you would like to analyze: ")
    prompt2 = ""

    while True:
        if not os.path.isfile(prompt1):
            print("File does not exist. Please enter a valid file name.")
            prompt1 = input("Please enter the file you would like to analyze: ")
        else:
            with open(prompt1, "r") as sequence:
                rawFile = sequence.read()
                if not rawFile.startswith('>'):
                    print("The file is not in FASTA format. Please try again.")
                else:
                    lines = rawFile.split('\n')
                    sequence_lines = lines[1:]
                    sequence = ''.join(sequence_lines)
                    if re.search(r'[^ATGC\n]', sequence):
                        print("Invalid FASTA format. Please make sure the sequence is in FASTA format.")
                    else:
                        break

    while prompt2 != "Q":
        prompt2 = input("What function would you like to run? Type 'A' to calculate DNA composition, Type 'B' to calculate AT content, Type 'C' to calculate GC content, Type 'D' to print the complement, Type 'E' to print the reverse complement, Type 'Q' to quit: ").upper()

        sequence = open(prompt1, "r")
        rawFile = sequence.read()
        firstLine = re.search(r'^.*?\n', rawFile).group()
        newFile2 = re.sub(re.escape(firstLine), '', rawFile, count=1)
        fasta = newFile2.replace("\n", "")


        if prompt2 == "A":
            dna_Comp(fasta)
        elif prompt2 == "B":
            at_Comp(fasta)
        elif prompt2 == "C":
            gc_Comp(fasta)
        elif prompt2 == "D":
            compliment(fasta)
        elif prompt2 == "E":
            reverse_Compliment(fasta)
        elif prompt2 == "Q":
            print("Program terminated")
            break

if __name__ == "__main__":
    mother_function()
