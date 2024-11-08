import re

sequence = ""
with open("sequence.fasta") as f:
    lines = f.readlines()
    sequence = ''.join(line.strip() for line in lines[1:]).upper()
    
g_count = sequence.count('G')
c_count = sequence.count('C')
total_count = len(sequence)
gc_percent = ((g_count + c_count) / total_count) * 100

print(f"G Count: {g_count}")
print(f"C Count: {c_count}")
print(f"Total Count: {total_count}")
print(f"GC Percent: {gc_percent:.2f}%")

a_count = sequence.count('A')
t_count = sequence.count('T')
at_percent = ((a_count + t_count) / total_count) * 100
print(f"A Count: {a_count}")
print(f"T Count: {t_count}")
print(f"AT Percent: {at_percent:.2f}%")

ratio = (a_count + t_count) / (g_count + c_count)
print(f"AT/GC Ratio: {ratio:.2f}")
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

coding_regions = []

start_index = sequence.find(start_codon)
# print(start_index)

while start_index != -1:
    for stop_codon in stop_codons:
        stop_index = sequence.find(stop_codon, start_index + 3)
        if stop_index != -1 and (stop_index - start_index) % 3 == 0:
            coding_region = sequence[start_index:stop_index + 3]
            coding_regions.append(coding_region)
            break
    start_index = sequence.find(start_codon, start_index + 1)

    
if coding_regions:
    print("Coding Regions Found")
    for i, coding_region in enumerate(coding_regions, start=1):
        print(f"\nRegion {i}: {coding_region}\nLength: {len(coding_region)}")
else:
    print("No coding regions found")

def find_motifs(sequence, motif):
    print(f"\nSearching for motif: {motif}")
    matches = [match.start() for match in re.finditer(motif, sequence)]
    if matches:
        print(f"Motif '{motif}' found at positions: {matches}")
    else:
        print(f"Motif '{motif}' not found")

# motifs = ['TATAA', 'ATTGCGCAAT', 'GGGCGG']  # TATA box, C/EBP binding site, CpG island motif
motif = "TATAA"

# for motif in motifs:
#     find_motifs(sequence, motif)

find_motifs(sequence, motif)