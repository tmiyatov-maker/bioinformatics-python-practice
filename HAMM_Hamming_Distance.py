"""
Rosalind Problem: HAMM - Hamming Distance

Description:
Counts the number of positions where two DNA strings differ.

Concepts:
- Loops
- Indexing
- Conditional statements
- Mutation comparison
"""

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

count = 0

for i in range(len(s)):
    if s[i] != t[i]:
        count += 1

print(count)
