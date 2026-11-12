#!/usr/bin/python3
def find_motif(motif, sequence):
    if not (3 <= len(motif) <=  7):
        return False
    positions = []
    count = 0
    for i in range(len(sequence) - len(motif) + 1):
       if  sequence[i:i+len(motif)] == motif:
           count +=1
           positions.append(i + 1)
    return count, positions

print(find_motif('ATG','ATGGGGTTTATGATGGGTGTGTGATGATG'))

