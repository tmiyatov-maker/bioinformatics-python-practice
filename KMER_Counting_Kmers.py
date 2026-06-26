"""
Practice Problem: k-mer Counting

Description:
Counts all substrings of length k in a DNA sequence.

Concepts:
- Dictionaries
- Sliding window
- Sequence pattern counting
"""

dna = "ATATAT"
k = 2

counts = {}

for i in range(len(dna) - k + 1):
    kmer = dna[i:i + k]

    if kmer in counts:
        counts[kmer] += 1
    else:
        counts[kmer] = 1

print(counts)
