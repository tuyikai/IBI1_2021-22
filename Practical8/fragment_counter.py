import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'# restore the code

a = re.findall('GAATTC', seq)# find all kind GAATTC

print(len(a) + 1)