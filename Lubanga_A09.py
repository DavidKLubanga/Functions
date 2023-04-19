#David Lubanga
#Assignment 09
#04/19/2023

#1


def name_major():
    print("David Lubanga, Biotechnology")
    
name_major()



#2


def gc_content(dna):
#    counter = input("Please input your DNA sequence in all caps: ")
#    counter = counter.upper()
    gc_count = dna.count("C" + "G")
#    dna_length = len(counter)
    gc_percent = gc_count/len(dna)
    print("The GC content of your DNA sequence is:" + str(gc_percent*1000) + "%")
    return gc_percent
    
result = gc_content("CCCCCGGGGGTTAAAA")
print(result)



#3


def timesTen(num):
    tenfold = int(num) * 10
    print(tenfold)
    return tenfold

multiplied = timesTen("3")    
print(multiplied)




#4


def average(num1, num2, num3):
    avg = (num1 + num2 + num3)/3
#    print(avg)
    return avg

final = average(3, 3, 4)
print(final)







