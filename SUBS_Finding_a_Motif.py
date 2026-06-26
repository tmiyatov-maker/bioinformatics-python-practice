"""
Rosalind Problem: SUBS - Finding a Motif in DNA

Description:
Finds all starting positions where a substring appears in a DNA sequence.

Concepts:
- Slicing
- Sliding window
- Motif search
"""

s = "GATATATGCATATACTT"
t = "ATAT"

positions = []

for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
        positions.append(i + 1)

print(positions)
