seq_human = "MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
seq_mouse = "MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
seq_random = "GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP"
edit_distance = 0
for a in range(len(seq_human)):
    if seq_human[a] != seq_mouse[a]:       
        edit_distance += 1
print(edit_distance)
edit_distance = 0
for a in range(len(seq_human)):
    if seq_human[a] != seq_random[a]:       
        edit_distance += 1
print(edit_distance)
edit_distance = 0
for a in range(len(seq_mouse)):
    if seq_mouse[a] != seq_random[a]:       
        edit_distance += 1# we can use this to memory some important information
print(edit_distance)



#  we compare the edit distance and find that the distance between human and mouse is only 10, while human to random and 
#  so human and mouse are very similar comparing to the random.
# meanwhile, i also write a local alignment program, the results between human and mouse are like below:
'''
MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGS-AGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY
MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAG-YPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY
{22: 'Q => P', 51: 'T => A', 53: 'G => A', 84: '- => A', 87: 'S => -', 97: 'S => G', 101: 'S => P', 117: 'N => S', 124: 'T => A', 262: 'T => P'}

MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSA-GSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY
MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAG-YPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY
{22: 'Q => P', 51: 'T => A', 53: 'G => A', 85: '- => A', 87: 'S => -', 97: 'S => G', 101: 'S => P', 117: 'N => S', 124: 'T => A', 262: 'T => P'}
'''
