#David Lubanga
#Assingment 11
#04-30-2023


#1

readFile = open('hmw11.txt', 'r')
accInfo = readFile.read()

accSeqs = dict()
for x in readFile:
    info = x.split(",")
    accSeqs[info[0].strip()] = info[1].strip()

readFile.close()
print(accSeqs)

#accFile = {cleanFile2}
#print(accFile)

readFile.close()


#2

import re

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


dna = input("Please input your DNA sequence: ")

protein = ""

for start in range(0,len(dna),3):
    codon = dna[start:start+3]
    aa = gencode.get(codon)
    protein = protein + aa
    #print("This is the corresponding protein sequence: " + codon)
    #print("the amino acid is " + aa)
print("The protein sequence is: " + protein)






