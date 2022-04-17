import re,os
name = input('Please input the fastq name:') 
#it's the input 
a = open('./'+ name)
b = open('./new_'+ name,'w')
seq = a.read()
pattern = re.compile('(.*?)_.*?Acc:.*?](.*?)>',re.S) # it uses compile to find pattern
seq_list = pattern.findall(seq)
for i in range(len(seq_list)):# it 
    if 'GAATTC' in seq_list[i][1]:# check GAATTC code
        a = re.sub(r'\n','',seq_list[i][1])
        b = re.findall('GAATTC', a)
        b.write('>' + f'{seq_list[i][0]:10}{len(b) + 1:10d}' + '\n')
        b.write(a + '\n')
a.close()
b.close()# it can close the code