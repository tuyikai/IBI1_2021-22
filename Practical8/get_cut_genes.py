import re,os
a = open('./Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')# open the file
b = open('./cut_genes.fa','w')# create a new file to restore the code
seq = a.read()# make use of the code
pattern = re.compile('(.*?)_.*?Acc:.*?](.*?)>',re.S)# find pattern of the code
seq_list = pattern.findall(seq)
for i in range(len(seq_list)):
    if 'GAATTC' in seq_list[i][1]:
        a = re.sub(r'\n','',seq_list[i][1])
        b.write('>' + f'{seq_list[i][0]:10}{len(a):10d}' + '\n')
        b.write(a + '\n')
a.close()
b.close()