
from numpy import kaiser


input= ('atgcgtagtcaATCGATGTAGCTAGTGACTGA').upper()#input = ('the word you want to code ')AND .UPPER CAN TURE THE WORD AN UPPER WORD
b= list(input)# it turns the input become a word and a word so that we can use it easily 
m = 0
n = 0 
o = 0
p = 0# these four are the count to remember

for i in range (len(b)):
    if b[i] == 'A':
        n +=1  
    elif b[i] == 'T':
        m +=1
    elif b[i] == 'C':
        o +=1
    elif b[i] == 'G':
        p +=1
print(n)
print('the percentage of A is ',n/len(b))
print('the percentage of G is ',p/len(b))
print('the percentage of T is ',m/len(b))
print('the percentage of C is ',o/len(b))
print(b)# print the result 